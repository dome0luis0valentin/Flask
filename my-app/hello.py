from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home/<name>/")
def home(name):
	return render_template('home.html', name = name)
@app.route('/')
def hello():
	return 'Hola Mundo'
