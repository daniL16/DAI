import flask
import os.path
from flask import *

app = flask.Flask(__name__)
#init_app(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=["POST"])
def login():
    session['username'] = request.form['user']
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='True')