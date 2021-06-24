from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo

# hash password and check password
from werkzeug.security import generate_password_hash, check_password_hash

# turn data mongo legible in json format
from bson import json_util

# convert json information in bson (mongodb information)
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://127.0.0.1/pythonmongodb'

mongo = PyMongo(app)


@app.route('/users', methods=['POST'])
def create_user():
    # Receiving data
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if username and email and password:
        hashed_pass = generate_password_hash(password)
        id_mongo = mongo.db.users.insert({
            "username": username,
            "email": email,
            "password": hashed_pass,
        })
        response = {
            "id": str(id_mongo),
            "username": username,
            "password": hashed_pass,
            "email": email
        }
        return response
    else:
        response = not_found()
        return response


@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')


@app.route('/users/<id_mongo>', methods=['GET'])
def get_user(id_mongo):
    user = mongo.db.users.find_one({
        "_id": ObjectId(id_mongo)
    })
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")


@app.route('/users/<id_mongo>', methods=['DELETE'])
def delete_user(id_mongo):
    mongo.db.users.delete_one({
        "_id": ObjectId(id_mongo),
    })
    response = jsonify({"message": "User" + id_mongo + "was Deleted successfully"})
    return response


@app.route('/users/<id_mongo>', methods=['PUT'])
def update_user(id_mongo):
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    if username and email and password:
        hashed_password = generate_password_hash(password)
        mongo.db.users.update_one({"_id": ObjectId(id_mongo)}, {"$set": {
            "username": username,
            "password": hashed_password,
            "email": email
        }})
        response = jsonify({"message": "User" + id_mongo + "was updated successfuly"})
        return response


@app.errorhandler(404)
def not_found(error=None):
    # jsonify change code 200 http response
    response = jsonify({
        "message": "Resource Not Found:" + request.url,
        "status": 404
    })
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)
