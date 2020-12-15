from flask import Flask, render_template,redirect, url_for, request, session
from bson import ObjectId
from datetime import datetime
import hashlib
import time
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="domaci6"
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/raspored')
def raspored():
	mc = mydb.cursor()
	mc.execute("SELECT * FROM raspored")
	sve = mc.fetchall()
	profy = []
	for svey in sve:
		if svey[3] not in profy:
			profy.append(svey[3])
	
	uci = []
	for svey in sve:
		if svey[7] not in uci:
			uci.append(svey[7])

	return render_template("sve2.html",sve = sve, profy = profy, uci = uci)




if __name__ == '__main__':
	app.run(debug=True)