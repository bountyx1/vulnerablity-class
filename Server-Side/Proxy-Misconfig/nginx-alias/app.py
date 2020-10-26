from flask import Flask,make_response
#Run export FLASK_APP=bakend.py && flask run



app = Flask(__name__)
 
@app.route('/')
def index():
        return("Hello World!")

