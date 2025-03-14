from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = getenv('MONGO_URI')
mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def obtener_usuarios():
    users = mongo.db.users.find()
    output = []
    for user in users:
        output.append({
            'username':user['username'],
            'email':user['email']
        })
    return jsonify({'Resultado':output})

@app.route('/users', methods=['POST'])
def agregar_usuarios():
    username = request.json(['username'])
    email = request.json(['email'])
    user = mongo.db.users.insertOne({'username':username, 'email':email})
    id_usuario = mongo.db.users.find({'_id': user})
    resultado = {'username':id_usuario['username'], 'email':id_usuario['email']}
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)