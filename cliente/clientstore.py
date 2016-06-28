from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
	name = request.args.get('name',"")
	return WineByName(name)

def WineByName(name):
	wineSearched = requests.get('https://natural-bus-135323.appspot.com/wines?name='+name)
	return render_template('template.html', wine=name)

if __name__ == '__main__':
    app.run(debug=True)

