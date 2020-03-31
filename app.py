import os
from tkinter import Image

import flask
import target as target
from flask import Flask, render_template, request, flash, jsonify, send_file, url_for
from werkzeug.utils import redirect, secure_filename

app = Flask(__name__)

# books = [
#     {'id': 0,
#      'title': 'A Fire Upon the Deep',
#      'author': 'Vernor Vinge',
#      'first_sentence': 'The coldsleep itself was dreamless.',
#      'year_published': '1992'},
#     {'id': 1,
#      'title': 'The Ones Who Walk Away From Omelas',
#      'author': 'Ursula K. Le Guin',
#      'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
#      'published': '1973'},
#     {'id': 2,
#      'title': 'Dhalgren',
#      'author': 'Samuel R. Delany',
#      'first_sentence': 'to wound the autumnal city.',
#      'published': '1975'}
# ]


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


@app.route('/api/image', methods=['GET', "POST"])
def image():
    file = request.files['b.png']
    file_name = file.filename or ''
    destination = '/'.join([target, file_name])
    file.save(destination)
    # pil_image = Image.open(image2)
    # return "Hello image Rain!"
    print("hi")
    return "Hello image Rain!"


def allowed_file(filename, ALLOWED_EXTENSIONS=None):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/img', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['b.png']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))

    return print(allowed_file('b.png'))

if __name__ == '__main__':
    app.run()