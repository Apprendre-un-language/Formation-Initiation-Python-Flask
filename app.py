from flask import Flask, jsonify, request
from bson import ObjectId
from bson.json_util import dumps
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['MONGO_URI'] = "mongodb://localhost:27017/livre"

mongo = PyMongo(app)

@app.after_request
def after_request(request):
    request.content_type = "application/json"
    return request
@app.route('/home')
def home():
    return 'Hello World !'

@app.route('/json')
def json():
    dictionnaire = {"Hello": "World"}
    return dictionnaire

@app.route('/livres', methods=['GET'])
def all_books():
    livre = mongo.db.test.find()
    response = dumps(livre)
    return response

@app.route('/livre', methods=['POST'])
def add_book():
    _json = request.json
    if _json['titre'] and _json['description']:
        livre = {}
        livre['titre'] = _json['titre']
        livre['description'] = _json['description']
        mongo.db.test.insert(livre)
        response = jsonify('Un livre a bien été créé !')
        return response

@app.route('/livre/<id>', methods=['GET'])
def one_book(id):
    livre = mongo.db.test.find_one({'_id': ObjectId(id)})
    response = dumps(livre)
    return response

@app.route('/livre/<id>', methods=['DELETE'])
def delete_book(id):
    mongo.db.test.delete_one({'_id': ObjectId(id)})
    response = jsonify('Le livre a bien été supprimé')
    return response

@app.route('/livre/<id>', methods=['PATCH'])
def update_book(id):
    _json = request.json
    livre = mongo.db.test.find_one({'_id': ObjectId(id)})
    for key in _json.keys():
        if key in ['titre', 'description']:
            livre[key] = _json[key]
    mongo.db.test.replace_one({'_id': ObjectId(id)}, livre)
    return {}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)