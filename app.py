from flask import Flask, jsonify, request
from bson import ObjectId
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['MONGO_URI'] = "t"

mongo = pymongo()

@app.route('/home')
def home():
    return 'Hello World !'

@app.route('/json')
def json():
    dictionnaire = {"Hello": "World"}
    return dictionnaire


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
