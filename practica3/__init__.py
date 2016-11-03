import flask
from flask import Flask, session, redirect,render_template
from flask import url_for, escape, request
import shelve
import re
from flask_shelve import init_app
from collections import deque

app = flask.Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
init_app(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/usuario", methods=["POST"])
def nuevo_usuario():
    username = request.form["username"]
    if re.match(r"^([a-zA-Z0-9]+)$", username):
        db = shelve.open('shelve.db')
        if db.has_key("users:{}".format(username)):
            return redirect(url_for("registro"))
            
        else:
            db["users:{}".format(username)] = {
                "username": username,
                "password": request.form["password"],
                "name": request.form["name"],
                "email":    request.form["email"]
            }
            return redirect(url_for("index"))
    else:
        return redirect(url_for("registro"))
    
@app.route('/login',methods=["POST"])
def login():
    username = request.form["username"]
    db = shelve.open('shelve.db')
    key = "users:{}".format(username)
    if db.has_key(key) and db[key]["password"] == request.form["password"]:
        session["username"] = request.form["username"]
        session["history"] = []
        
    return redirect(url_for("index"))
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html',title=' Elementos flotantes y clearing')

    
@app.route('/usuario/datos')
def usuario():
    db = shelve.open('shelve.db')
    key = "users:{}".format(session["username"])
    user = db[key]
    return render_template("usuario.html", user=user)

@app.route('/usuario/modificar',methods=["GET","POST"])
def modificar_usuario():
    db = shelve.open('shelve.db')
    username = session["username"]
    if request.method=="POST":
        db["users:{}".format(username)] = {
                "username": username,
                "password": request.form["pass"],
                "name": request.form["name"],
                "email": request.form["email"]
            }
        return redirect(url_for("index"))
    else:
        key = "users:{}".format(username)
        user = db[key]
        return render_template("modificar_usuario.html", user=user)

@app.after_request
def save_history(response):
    if "username" in session and response.mimetype == "text/html":
            h = deque(session["history"], 3)
            h.appendleft(request.path)
            session["history"] = list(h)
    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='True')