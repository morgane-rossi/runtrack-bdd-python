import mysql.connector
import os

f = open("data.py", "r")
data = f.read()

username = data.personnel[0]
userpass = data.personnel[1]
