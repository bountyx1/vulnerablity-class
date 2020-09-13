from flask import Flask,request,render_template,redirect,make_response
from werkzeug.routing import BaseConverter
import hashlib 

app = Flask(__name__)

@app.route('/')
def index():
	return("Hello World!")

@app.route('/account/login',methods=["GET","POST"])
def login():
	if request.method=="GET":
		return render_template("login/login.html")
	else:
		if request.method=="POST":
			username = request.form["username"]
			password = request.form["password"]
			if username=="demo" and password=="demo":
				response = make_response(render_template("login/redirect.html"))
				cookie_value = hashlib.md5('demo:demo'.encode()) 
				response.set_cookie("user",cookie_value.hexdigest())
				return response
			else:
				 return("Invalid creds try demo/demo")

@app.route('/main.js',methods=["GET"])
def mainjs():
	token = request.cookies.get('user')
	return render_template('dashboard/main.js',token=token)

@app.route('/account/dashboard',methods=["GET","POST"])
def dashboard():
	if request.cookies.get('user') == "80851851709e01bc9453cced585a7bca":
		return render_template("dashboard/dashboard.html")
	elif request.cookies.get('user') == "d98dbae3555d8c1229fc2db4ad14a391":
		#admin T!h!%sH@.^&*(/
		return("flag{W3b_C@che_D3c3pt!0N}")
	else:
		return("Please login")