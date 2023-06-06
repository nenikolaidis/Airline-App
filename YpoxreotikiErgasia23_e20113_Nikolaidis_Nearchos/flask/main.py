from flask import Flask, jsonify, request
from pymongo import MongoClient

client = MongoClient("172.19.0.1",27017)
db = client["database"]
users_collection = db["users_collection"]
flights_collection = db["flights_collection"]

app = Flask(__name__)

@app.route("/")
def base():
    pass

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True, port = 5000)