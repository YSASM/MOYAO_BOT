from datetime import datetime
from functools import reduce
import random
from flask import Flask,render_template,url_for,request
import MySQLdb
db = MySQLdb.connect("localhost", "root", "root", "qq_bot", charset='utf8' )
cursor = db.cursor()
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    freeuse = 10
    freeunuse = 20
    cpuuse=30
    cpuunuse=10
    return render_template('index.html',
    freeuse=freeuse,
    freeunuse=freeunuse,
    cpuuse=cpuuse,
    cpuunuse=cpuunuse
    )
@app.route("/plug",methods=['GET','POST'])
def plug():
    return render_template('plug.html')
app.run()