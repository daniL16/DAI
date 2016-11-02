from flask import Flask,current_app,request
import mandelbrot
import os.path

app = Flask(__name__)

@app.route('/')
def index():
    print 'Para acceder al fractal : /fractal'
    
    
@app.route('/fractal',methods=['GET'])
def formulario():
    if request.args.get('x1') is None:
         return current_app.send_static_file('formulario_get.html')
    else:
        x1 = request.args.get('x1')
        x2 = request.args.get('x2')
        y1 = request.args.get('y1')
        y2 = request.args.get('y2')
        ancho = request.args.get('ancho')
        iteraciones = request.args.get('iteraciones')
        nombre=x1+x2+y1+y2+ancho+iteraciones+'.png'
        ruta='./app/static/'+nombre
        
        if  os.path.exists(ruta):
            return current_app.send_static_file(nombre)
        else:
            mandelbrot.renderizaMandelbrot(float(x1),float(y1), float(x2), float(y2), int(ancho), int(iteraciones), ruta)
            return current_app.send_static_file(nombre)
       
       
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='True')