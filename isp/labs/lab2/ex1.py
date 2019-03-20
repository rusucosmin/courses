from flask import Flask, request
import base64
import json

app = Flask(__name__)

mySecureOneTimePad = "Never send a human to do a machine's job";

def superencryption(msg, key):
  if len(key) < len(msg):
    diff = len(msg) - len(key)
    key += key[0:diff]
  amsg = list(map(ord, msg))
  akey = list(map(ord, key[0:len(msg)]))

  aux = "".join(map(lambda x: chr(x[1] ^ akey[x[0]]), enumerate(amsg)))
  aux = bytes(aux, 'utf-8')
  return base64.b64encode(aux)


def checklogin(user, pwd, key):
  enc = superencryption(user, key)
  return enc == bytes(pwd, 'utf-8')

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/hw2/ex1", methods=['POST'])
def login():
  data = json.loads(request.data.decode('utf-8'))
  user = data["user"]
  pwd = data["pass"]
  if checklogin(user, pwd, mySecureOneTimePad):
    return '', 200
  else:
    return '', 400

app.run()
