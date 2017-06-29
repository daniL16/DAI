import flask
import shelve
import os.path

from flask import *
from flask_shelve import init_app

app = flask.Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
init_app(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/<user_name>')
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

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='True')