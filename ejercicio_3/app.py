from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from dotenv import loadotenv
from os import getenv
loadotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = getenv('MONGO_URI')
mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def obtener_usuarios():
    users = mongo.db.usuarios.find()
    output = []

if __name__ == '__main__':
    app.run(debug=True)