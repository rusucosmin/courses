#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='monty',
                             password='python',
                             db='students',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `grades`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        # Create a new record
        sql = "INSERT INTO `grades` (`name`, `grade`) VALUES (%s, %s)"
        cursor.execute(sql, ('bryan', '6'))

        # Read a single record
        sql = "SELECT * FROM `grades`"
        cursor.execute(sql)
        result = cursor.fetchall()

        found = False
        for row in result:
            if row["name"] == "bryan" and int(row["grade"]) == 6:
                print("Victory is sweetest when you’ve known defeat.")
                found = True
        if not found:
            print("I can only show you the door. You're the one that has to walk through it.")

finally:
    connection.close()
