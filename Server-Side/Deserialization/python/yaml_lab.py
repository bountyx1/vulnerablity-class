from flask import Flask,request,render_template,redirect,make_response
from werkzeug.routing import BaseConverter
import base64,yaml

app = Flask(__name__)
flag="{PICKE{Deserialization}}"

class Person:
  def __init__(self, name):
    self.name = name

@app.route('/')
def index():
	new_person = Person(request.args.get('user'))
	data=yaml.dump(new_person).encode()
	print(type(data))
	session_cookie = base64.b64encode(yaml.dump(new_person))
	return redirect("http://localhost:5000/api/?key="+session_cookie.decode())

@app.route('/api/')
def api():
	key = request.args.get('key')
	base=base64.b64decode(key)
	object = yaml.load(base)
	if object.name == None:
		object.name = "Anonymous User"
	return "Logged in as "+object.name
