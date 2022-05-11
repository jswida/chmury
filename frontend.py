#! /usr/bin/env python
from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    r = requests.get('http://localhost:5000')
    plants = r.json()
    return render_template('index.html', plants=plants[:100])


if __name__ == '__main__':
    app.run(debug=True, port=8080)