import flask
from flask import Flask, session, redirect,render_template,jsonify
from flask import url_for, escape, request
import shelve
import re
from flask_shelve import init_app
from collections import deque
import pymongo
import tweepy

app = flask.Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
init_app(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/highchart")
def highchart():
    return render_template("highchart.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/twitter")
def twitter():
    # Consumer keys and access tokens, used for OAuth
    consumer_key = 'mNqfsXYES7CHKpCLi1fp8J5yT'
    consumer_secret = 'uapqEQVl95rKOY2NMbLTw5vL2pmj0YT1glzpTi7Esbhk0Il8fh'
    access_token = '268808881-L9Zt2aCRL4udK43Ke3HUn4zXW9MtpI2Wgo7zWKJY'
    access_token_secret = '9HnMe1w8q65Ps661EHiOJOZ3NliKW58NM4vmShX65RH12'
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
    tweets = api.search(q='Granada', count=1)
    print(tweets[0].author)
    return render_template("map.html")
    
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

@app.route("/nuevo_restaurante", methods=["GET","POST"])
def nuevo_restaurante():
    if request.method=="POST":
        address = {"building":request.form["building"],
                  "street":request.form["street"],
                  "zipcode":request.form["zipcode"],
                  "coord":"["+request.form["coord1"]+","+request.form["coord2"]+"]"
                 }
        rest = {"name":request.form["name"],
            "borough":request.form["borough"],
            "cuisine":request.form["cuisine"],
            "address": address,
            "restaurant_id": request.form["rest_id"]
           }
        print rest
        collection.insert(rest)
        return redirect(url_for("index"))
    else:
        return render_template("nuevo_restaurante.html")

@app.route("/modificar_restaurante", methods=["GET","POST"])
def modificar_restaurante():
    if request.method=="POST":
        address = {"building":request.form["building"],
                  "street":request.form["street"],
                  "zipcode":request.form["zipcode"],
                  "coord":"["+request.form["coord1"]+","+request.form["coord2"]+"]"
                 }
        rest = {"name":request.form["name"],
            "borough":request.form["borough"],
            "cuisine":request.form["cuisine"],
            "address": address,
            "restaurant_id": request.form["rest_id"]}
        
        id = request.form["rest_id"];
        print collection.update({"restaurant_id":id},rest);
        return redirect(url_for("index"))
    else:
        id = request.args.get('id');
        rest = collection.find_one({"restaurant_id":id});
        return render_template("modificar_restaurante.html",rest=rest)

@app.route("/buscar_restaurante", methods=["GET","POST"])
def buscar_restaurante():
    if request.method=="POST":
        zipcode = request.form['zipcode'];
        cuisine = request.form['cuisine'];
        print zipcode;
        if (zipcode != "" and cuisine != ""):
            restaurants = collection.find({"zipcode":zipcode,"cuisine":cuisine}).sort([("name", pymongo.ASCENDING)]);
        elif(zipcode != ""):
            restaurants = collection.find({"zipcode":zipcode}).sort([("name", pymongo.ASCENDING)]);
        elif (cuisine != ""):
            restaurants = collection.find({"cuisine":cuisine}).sort([("name", pymongo.ASCENDING)]);
        else:
            restaurants = collection.find().sort([("name", pymongo.ASCENDING)]);
        return render_template("mostrar_restaurante.html",restaurants=restaurants)
    else:
        return render_template("busqueda.html")
    
    
@app.route("/puntuar_restaurante", methods=["GET","POST"])
def puntuar_restaurante():
    if request.method=="POST":
        grade = request.form['grade'];
        score = request.form['score'];
    else:
        return render_template("range.html",id);
    
@app.route('/quiero_filas_desde_la')
def devuelve_filas():
    desde = request.args.get('fila', '',)
    filas = db.restaurants.find().skip(int(desde)).limit(10)
    #return jsonify(filas)


if __name__ == '__main__':
    try:
        conn=pymongo.MongoClient()
        db = conn.p4
        collection = db.restaurants
        print "Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e 
    print collection
    app.run(host='0.0.0.0',debug='True')
    