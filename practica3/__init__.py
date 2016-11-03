from flask import Flask, session, redirect,render_template
from flask import url_for, escape, request

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

def ultima():
    try:
        session['ultima'] = (session['ultima']+1)%3
        return session['ultima']
    except KeyError:
        session['ultima'] = 0
@app.route('/index')
def index():
    ult = ultima()
    session[ult]='index.html'
    return render_template('index.html')

@app.route('/page2')
def page2():
    ult = ultima()
    session[ult]='page2.html'
    return render_template('page2.html')

@app.route('/page3')
def page3():
    ult = ultima()
    session[ult]='page3.html'
    return render_template('page3.html')

@app.route('/',methods=["POST"])
def login():
    if request.method== 'POST':
        session['username'] = request.form['username']
        return render_template('index.html')
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='True')