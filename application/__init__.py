from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "2e7be4c51fd348842af153b2c5e658a479bae960"
app.config["MONGO_URI"] = "mongodb://localhost:27017/fundamental"

mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes