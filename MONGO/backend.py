import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

cluster = MongoClient("mongodb+srv://ravenaa:1234@cluster0.45c07.mongodb.net/test?retryWrites=true&w=majority")

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# database name
db = cluster["test"]
collection = db["users"]

@app.route("/register", methods=["POST", "GET"])
@cross_origin()
def register():
    if request.method == 'POST':
        
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        posts = {"name": name,"email":email,"password":password}
        collection.insert_one(posts)

      
        
        data = {'name':str(name),'email':str(email)}
        return jsonify(data)

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        name = request.json["name"]
        password = request.json["password"]

        status = collection.find_one({'name':name,'password':password})
        if status==None:
            return jsonify({"message":"Login failed !"})
        else:
            return jsonify({"message" : "Login Verified !"})


if __name__ == '__main__':
    app.run(host="localhost",port =8000,debug=True)