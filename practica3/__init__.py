from flask import Flask, session, redirect,render_template
from flask import url_for, escape, request
import shelve
import re

app = Flask(__name__)
shelve.open('shelve.db')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def ultima():
    try:
        session['ultima'] = (session['ultima']+1)%3
        return session['ultima']
    except KeyError:
        session['ultima'] = 0
        

@app.route("/")
def index():
    if "username" in session:
        return render_template("index_logged.html", username=session["username"])
    else:
        return render_template("index.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/usuario", methods=["POST"])
def nuevo_usuario():
    username = request.form["username"]
    if re.match(r"^([a-zA-Z0-9]+)$", username):
        db = shelve.get_shelve('c')
        if "users:{}".format(username) not in db:
            db["users:{}".format(username)] = {
                "username": username,
                "password": request.form["password"],
                "realname": request.form["realname"],
                "email":    request.form["email"]
            }
            return redirect(url_for("index"))
        else:
            return redirect(url_for("registro"))
    else:
        return redirect(url_for("registro"))
        return redirect(url_for("registro"))


@app.route('/page1')
def page1():
    ult = ultima()
    session[ult]='page1.html'
    return render_template('page1.html')

@app.route('/page2')
def page2():
    ult = ultima()
    session[ult]='page2.html'
    return render_template('page2.html')

@app.route('/login',methods=["POST"])
def login():
    if request.method== 'POST':
        session['username'] = request.form['username']
        return render_template('index.html')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='True')