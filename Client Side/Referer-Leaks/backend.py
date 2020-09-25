from flask import Flask,request,render_template,redirect,make_response
from werkzeug.routing import BaseConverter
import hashlib 

app = Flask(__name__)

@app.route('/')
def index():
	result=hashlib.md5(b'testtokenleak') 
	result=result.hexdigest()
	return redirect("/reset?name="+str(result))

@app.route('/reset')
def reset():
	name = request.args.get("name")
	html ="""
	<h1>Hello world</h1>
	//https
	<a href="https://localhost:5000">Click me
	<script src="https://localhost:5000/file.js"></script>
	<script src="https://localhost:5000/test.js" rel="noreferrer"></script>
	"""
	return html


	@app.route('/')
def index():
        new_person = Person(request.user.get('name'))
        session_cookie = base64.b64encode(pickle.dumps(new_person))
        redirectsession_cookie
