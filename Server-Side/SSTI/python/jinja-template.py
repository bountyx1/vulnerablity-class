from flask import Flask,request,render_template_string,redirect,make_response
from werkzeug.routing import BaseConverter

app = Flask(__name__)
flag = "ssti{jinja<3ssti}"
@app.route('/')
def index():
	name = request.args.get("name")
	template="""
	<h1> Hello world</h1>
	<br>
	<h4> Hello {}</h4>
	""".format(name)
	return render_template_string(template)

