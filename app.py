#!/usr/bin/python3.11

from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
