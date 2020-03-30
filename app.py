import os
import flask
from flask import Flask, render_template, request, flash, jsonify, send_file


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    return "Hello World Rain!"


# upload selected image and forward to processing page
@app.route("/download", methods=['GET', 'POST'])
def download():
    if request.args.get('type') == '1':
        filename = 'b.png'
    else:
        filename = 'b.png'
    return send_file(filename, mimetype='b/png')


if __name__ == '__main__':
    app.run()
