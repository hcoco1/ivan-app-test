#!/usr/bin/env python3
from flask_cors import cross_origin
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db
from models import User, Post
from flask import Flask




@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
