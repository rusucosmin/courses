from flask import Flask, request
import base64
import json
import bcrypt

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/hw4/ex2", methods=['POST'])
def login():
  data = json.loads(request.data.decode('utf-8'))
  user = data["user"]
  pwd = data["pass"].encode('utf-8')
  pwd_hash = bcrypt.hashpw(pwd, bcrypt.gensalt())
  return pwd_hash, 200

app.run()

