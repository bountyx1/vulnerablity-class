from flask import Flask,request,render_template,redirect,make_response
from werkzeug.routing import BaseConverter

app = Flask(__name__)

flag = "flag{I <3 Format String}"
class User:
	def __init__(self,name):
		self.name=name
	def message(self,message,obj):
		return message.format(user=obj)
@app.route('/')
def index():
	user = User(request.args.get("name"))
	x=user.message(request.args.get('message'),user)
	return x



