import flask
import shelve
import os.path
import pymongo
import tweepy
import feedparser

from flask import *
from flask_shelve import init_app

#credenciales twwepy
consumer_key = 'mNqfsXYES7CHKpCLi1fp8J5yT'
consumer_secret = 'uapqEQVl95rKOY2NMbLTw5vL2pmj0YT1glzpTi7Esbhk0Il8fh'
access_token = '268808881-L9Zt2aCRL4udK43Ke3HUn4zXW9MtpI2Wgo7zWKJY'
access_token_secret = '9HnMe1w8q65Ps661EHiOJOZ3NliKW58NM4vmShX65RH12'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

app = flask.Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
init_app(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    rss_url = "http://www.microsiervos.com/index.xml"
    feed = feedparser.parse( rss_url )
    return render_template('index.html',feed=feed['entries'])

@app.route('/login',methods=["POST"])
def login():
    db = shelve.open('shelve.db');
    key = request.form['user']
    if (key in db):
        if (db[key]['pass'] == request.form['pass']):
            session['username'] = request.form['user']
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')

@app.route('/registroUsuario')
def registro():
    return render_template('registroUsuario.html')

@app.route('/nuevoUsuario',methods=['POST'])
def nuevoUsuario():
    db = shelve.open('shelve.db');
    key = request.form['nombre'];
    if ( key in db):
        print ("Usuario ya registrado");
    else :
        db[key]={'name':key, 'pass' :request.form['pass'], 'email':  request.form['email']};
    return render_template('index.html')

@app.route('/usuarios/<user_name>')
def echo_usuario(user_name):
    db = shelve.open('shelve.db');
    user = db[user_name];
    return render_template('editarUsuario.html',user=user)

@app.route('/editarUsuario',methods=['post'])
def editarUsuario():
    db = shelve.open('shelve.db');
    key = request.form['nombre'];
    db[key]={'name':key, 'pass' :request.form['pass'], 'email':  request.form['email']};
    return render_template('index.html')

@app.route('/restaurantes',methods=['post','get'])
def restaurantes():
    if (request.method == 'GET'):
        if (len (request.args.get('cuisine')) > 0 and len(request.args.get('borough')) > 0  ):
            rest = collection.find({'cuisine':request.args.get('cuisine'),'borough':request.args.get('borough')})
        elif(len (request.args.get('cuisine')) > 0):
            rest = collection.find({'cuisine':request.args.get('cuisine')})
        elif (len (request.args.get('borough')) > 0):
            rest = collection.find({'cuisine':request.args.get('borough')})
        else:
            rest = collection.find()
    else:
        rest = collection.find()
        
    return render_template('restaurantes.html',rest=rest)

@app.route('/registroRestaurante')
def registroRestaurante():
    return render_template('registroRestaurante.html')

@app.route('/editar/<rest_id>')
def editarRestaurante(rest_id):
    rest = collection.find({'restaurant_id': rest_id})
    return render_template('editarRestaurante.html',rest=rest)

@app.route('/restaurantes/<rest_id>')
def echo_restaurante(rest_id):
    rest = collection.find_one({'restaurant_id': rest_id})
    tweets = api.search(q=rest['name'], count=3)
    scores=[]
    for grade in rest['grades']:
        scores.append(grade['score'])
    return render_template('restaurante.html',rest=rest,tweets=tweets,scores=scores)

@app.route('/editarRestaurante',methods=['post'])
def editarRest():
    collection.update({'restaurant_id':request.form['id']},{'restaurant_id':request.form['id'],'name':request.form['nombre'], 'cuisine':request.form['cocina'], 'borough':request.form['borough'], 'address':{'zipcode':request.form['zipcode'],'street':request.form['street'],'building':request.form['building']}})
    
    rest = collection.find({'restaurant_id':request.form['id']})
    return render_template('restaurantes.html',rest=rest)

@app.route('/nuevoRestaurante',methods=['post'])
def nuevoRestaurante():
    collection.insert({'restaurant_id':request.form['id'], 'name':request.form['nombre'], 'cuisine':request.form['cocina'], 'borough':request.form['borough'], 'address':{'zipcode':request.form['zipcode'],'street':request.form['street'],'building':request.form['building']}})
    
    rest = collection.find({'restaurant_id':request.form['id']})
    return render_template('restaurantes.html',rest=rest)

@app.route('/borrarRestaurante/<rest_id>')
def borrarRestaurante(rest_id):
    collection.delete_one({'restaurant_id':rest_id})
    
    rest = collection.find()
    return render_template('restaurantes.html',rest=rest )

if __name__ == '__main__':
    #conexion DB
    try:
        conn=pymongo.MongoClient()
        db = conn.test
        collection = db.restaurants
        print ("Connected successfully!!!")
    except pymongo.errors.ConnectionFailure:
        print ("Could not connect to MongoDB: %s" )
    print (collection)
    app.run(host='0.0.0.0',debug='True')