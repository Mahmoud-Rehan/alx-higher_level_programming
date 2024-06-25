#!/usr/bin/python3
""" Lists all the states from a database hbtn_0e_0_usa"""
import MySQLdb


connection = MySQLdb.connect(user="root", passwd="root",
                             host="localhost", port=3306, db="hbtn_0e_0_usa")
cur = connection.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
connection.close()
