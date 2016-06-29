from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def start():
	return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)
