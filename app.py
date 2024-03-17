import os, io, zipfile
from flask import Flask, render_template, request, send_file
from rembg import remove

app = Flask(__name__)

@app.route('/')
def index():
    return (render_template('index.html'))


if __name__ == '__main__':
    app.run(debug=True)