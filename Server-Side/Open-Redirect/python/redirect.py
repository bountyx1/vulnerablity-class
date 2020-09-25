from flask import Flask,request,redirect,make_response
from werkzeug.routing import BaseConverter
from urllib.parse import urlparse

app = Flask(__name__)
@app.route('/')
def index():
	host = request.args.get("host")
	o=urlparse(host)
	print(o)
	return "<a href={}>clickme".format(host)

