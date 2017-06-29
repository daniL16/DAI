import flask
from flask import Flask, session, redirect,render_template,jsonify
from flask import url_for, escape, request
import shelve
import re
	from flask_shelve import init_app
from collections import deque
import pymongo
import tweepy
import feedparser

app = flask.Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'

consumer_key = 'mNqfsXYES7CHKpCLi1fp8J5yT'
consumer_secret = 'uapqEQVl95rKOY2NMbLTw5vL2pmj0YT1glzpTi7Esbhk0Il8fh'
access_token = '268808881-L9Zt2aCRL4udK43Ke3HUn4zXW9MtpI2Wgo7zWKJY'
access_token_secret = '9HnMe1w8q65Ps661EHiOJOZ3NliKW58NM4vmShX65RH12'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

init_app(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/map")
def maps():
    return render_template('mapa.html')
@app.route("/")
def index():
        rss = feedparser.parse('https://www.meneame.net/rss')
        entradas = rss.entries
        return render_template("index.html",noticias=entradas)

        
@app.route("/registro")
def registro():
    return render_template("registro.html")

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
        collection.update({"restaurant_id":id},rest);
        return redirect(url_for("index"))
    else:
        return render_template("busqueda.html")








@app.route("/buscar_restaurante", methods=["GET","POST"])
def buscar_restaurante():
    if request.method=="POST":
        zipcode = request.form['zipcode'];
        cuisine = request.form['cuisine'];
        
        if (zipcode != "" and cuisine != ""):
            restaurants = collection.find({"address.zipcode":zipcode,"cuisine":cuisine}).sort([("name", pymongo.ASCENDING)]).limit(10);
            rest = collection.find_one({"address.zipcode":zipcode,"cuisine":cuisine})
        elif(zipcode != ""):
            restaurants = collection.find({"address.zipcode":zipcode}).sort([("name", pymongo.ASCENDING)]).limit(10);
            rest = collection.find_one({"address.zipcode":zipcode})
        elif (cuisine != ""):
            restaurants = collection.find({"cuisine":cuisine}).sort([("name", pymongo.ASCENDING)]).limit(10);
            rest = collection.find_one({"cuisine":cuisine})
        else:
            restaurants = collection.find().sort([("name", pymongo.ASCENDING)]).limit(10);
            rest = collection.find_one()
       
       
        tweets = api.search(q=rest['name'], count=10)
        return render_template("mostrar_restaurante.html",restaurants=restaurants,rest = rest,tweets=tweets)
    
        
    else:
        return render_template("busqueda.html")





    
@app.route("/info")
def info():
    restaurantes = collection.find()
    
    #restaurantes por barrio
    brooklyn = db.restaurants.find({'borough':"Brooklyn"}).count();
    brooklyn_ch = db.restaurants.find({'borough':"Brooklyn",'cuisine':"Chinese"}).count();
    brooklyn_it = db.restaurants.find({'borough':"Brooklyn",'cuisine':"Italian"}).count();
    brooklyn_am = db.restaurants.find({'borough':"Brooklyn",'cuisine':"American "}).count();
    brooklyn_spa = db.restaurants.find({'borough':"Brooklyn",'cuisine':"Spanish"}).count();
    manhattan = db.restaurants.find({'borough':"Manhattan"}).count();
    manhattan_ch = db.restaurants.find({'borough':"Manhattan",'cuisine':"Chinese"}).count();
    manhattan_it = db.restaurants.find({'borough':"Manhattan",'cuisine':"Italian"}).count();
    manhattan_am = db.restaurants.find({'borough':"Manhattan",'cuisine':"American "}).count();
    manhattan_spa = db.restaurants.find({'borough':"Manhattan",'cuisine':"Spanish"}).count();
    matriz = [[brooklyn,brooklyn_ch,brooklyn_it, brooklyn_am,brooklyn_spa],[ manhattan, manhattan_ch,manhattan_it,manhattan_am,manhattan_spa]]
    
    #coordenadas
    coord=[];
    for r in restaurantes:
        coord.append([r["name"],r["address"]["coord"]])

    return render_template("info.html",matriz=matriz,coords=coord)



@app.route('/quiero_filas_desde_la')
def devuelve_filas():
    desde = request.args.get('fila', '',)
    filas = db.restaurants.find().skip(int(desde)).limit(10)
    return jsonify(filas)






@app.route("/usuario", methods=["POST"])
def nuevo_usuario():
    username = request.form["username"]
    db = shelve.open('shelve.db')
    db["users:{}".format(username)] = {
                "username": username,
                "password": request.form["password"],
                "name": request.form["name"],
                "email":    request.form["email"]
            }
    return redirect(url_for("index"))
    
    
@app.route('/login',methods=['GET', "POST"])
def login():
    if request.method=="POST":
        username = str(request.form["username"])
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
    
