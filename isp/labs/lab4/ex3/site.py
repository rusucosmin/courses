#!/usr/bin/env python3
import os
import sys
import populate
from flask import g
from flask import Flask, current_app
from flask import render_template, request, jsonify
import pymysql


app = Flask(__name__)
username = "root"
password = "root"
database = "hw4_ex3"

## This method returns a list of messages in a json format such as
## [
##  { "name": <name>, "message": <message> },
##  { "name": <name>, "message": <message> },
##  ...
## ]
## If this is a POST request and there is a parameter "name" given, then only
## messages of the given name should be returned.
## If the POST parameter is invalid, then the response code must be 500.
@app.route("/messages",methods=["GET","POST"])
def messages():
    with db.cursor() as cursor:
        json = []
        row_list={}

        if (request.method == "POST"):
            name_request = request.values.get("name")
            if(name_request is None):
                abort(500)
            cursor.execute('select * from messages where name like %s', name_request)
        else:
            cursor.execute('select * from messages')

        row = cursor.fetchone()
        while row:
            row_list = {"name": row[0], "message": row[1]}
            json.append(row_list)
            row = cursor.fetchone()

        return jsonify(json), 200

## This method returns the list of users in a json format such as
## { "users": [ <user1>, <user2>, ... ] }
## This methods should limit the number of users if a GET URL parameter is given
## named limit. For example, /users?limit=4 should only return the first four
## users.
## If the paramer given is invalid, then the response code must be 500.
@app.route("/users",methods=["GET"])
def contact():
    with db.cursor() as cursor:
        limit_param = request.args.get('limit')
        json = []

        if (limit_param is None):
            cursor.execute('select name from users')
        else:
            limit_param_new = limit_param.split("'")
            if (len(limit_param_new) > 1):
                #There is an injection attempt
                abort(500)
            cursor.execute('select name from users limit %s', int(limit_param_new[0]))

        row = cursor.fetchone()
        while row:
            json.append(row[0])
            row = cursor.fetchone()

        result = {"users": json}
        return jsonify(result), 200

if __name__ == "__main__":
    seed = "randomseed"
    if len(sys.argv) == 2:
        seed = sys.argv[1]

    db = pymysql.connect("localhost",
                username,
                password,
                database)
    with db.cursor() as cursor:
        populate.populate_db(seed,cursor)
        db.commit()
    print("[+] database populated")

    app.run(host='0.0.0.0',port=80)
