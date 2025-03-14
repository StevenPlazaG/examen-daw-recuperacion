from flask import Flask
from os import getenv

app = Flask(__name__, static_folder='static')

NODO = getenv('NODO')

@app.route('/')
def index():
    if NODO == '1':
        imagen = './static/1.png'
    elif NODO == '2':
        imagen = './static/2.png'
    elif NODO == '3':
        imagen = './static/3.png'
    return f'''
        <head><title>Nodo {NODO}</title></head>
        <body>
            <h1>Bienvenido al Nodo {NODO}</h1>
            <img src={imagen}>
        </body>
        '''

@app.route('about')
def about():
        return f'''
        <head><title>Nodo {NODO}</title></head>
        <body>
            <h1>Bienvenido al abour del nodo {NODO}</h1>
        </body>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)