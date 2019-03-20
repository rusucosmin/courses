from flask import Flask, request, make_response
import base64
import json
import hmac
import hashlib

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

key = "LQoFCBtOXRcbF1UhRRgTAU8NSA=="

def sha256(msg):
  return int(hashlib.sha256(msg.encode('utf-8')).hexdigest(), 16)

def hmac_sha256(key, msg):
  signature = hmac.new(bytes(key, 'latin-1'),
    msg = bytes(msg, 'latin-1'),
    digestmod = hashlib.sha256).hexdigest().upper()
  return signature

@app.route("/ex3/login", methods=['POST'])
def login():
  data = json.loads(request.data.decode('utf-8'))
  user = data["user"]
  pwd = data["pass"]
  resp = make_response()
  if user == "administrator" and pwd == "42":
    cookie = 'administrator,1489662453,com402,hw2,ex3,administrator'
    hmac = hmac_sha256(key, cookie)
    cookie = cookie + "," + hmac
    cookie = base64.b64encode(cookie.encode('utf-8'))
    resp.set_cookie('LoginCookie', cookie)
  else:
    cookie = "Yoda,1563905697,com402,hw2,ex3,user"
    hmac = hmac_sha256(key, cookie)
    cookie = cookie + "," + hmac
    cookie = base64.b64encode(cookie.encode('utf-8'))
    resp.set_cookie('LoginCookie', cookie)
  return resp


@app.route("/ex3/list", methods=['POST'])
def list():
  loginCookie = request.cookies.get('LoginCookie')
  loginCookie = base64.b64decode(loginCookie).decode('utf-8')
  user, user_id, com402, hw2, ex3, user_role, hmac = loginCookie.split(',')
  hmac_role = hmac_sha256(key, ','.join([user, user_id, com402, hw2, ex3, user_role]))
  if hmac_role != hmac:
    return '', 403
  elif user_role == "user":
    return '', 201
  else:
    return '', 200

app.run()
