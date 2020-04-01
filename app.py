from typing import io

import PIL.Image
import flask

from flask import Flask, request, send_file
from imageio import imread
from werkzeug.utils import secure_filename
import cv2

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    return "Hello World Rain!"


# download selected image and forward to processing page
@app.route("/download", methods=['GET', 'POST'])
def download():
    if request.args.get('type') == '1':
        filename = 'b.png'
    else:
        filename = 'b.png'
    return send_file(filename, mimetype='b/png')


# upload selected image and forward to processing page
@app.route("/upload", methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded'


@app.route("/img", methods=['GET', 'POST'])
def img():
    if request.args.get('type') == '1':
        filename = request.files['file']
        image = PIL.Image.open(filename)
        width, height = image.size
        response = width + height
    else:
        filename = request.files['file']
        image = PIL.Image.open(filename)
        width, height = image.size
        filename2 = secure_filename(filename.filename)

        # imgt = PIL.Image.open(r'c:\temp\temp.jpg')
        filepath = image.filename

        # img = cv2.imread('b.png')
        # x=str(img.shape)


        # image2 = io.imread(filename, plugin='matplotlib')
        img = cv2.imread('01.jpeg')
        if (len(img.shape) < 3):
            x = 'gray'
            y = str(img.shape)
        elif len(img.shape) == 3:
            x = 'Color(RGB)'
            y = str(img.shape)
        else:
            x = 'others'
            y = str(img.shape)

        response = "<h3>File name: </h3>" + filename2 + \
                   "<h3>Height & Width: </h3>" + str(height) + ",  " + str(width) + \
                   "<h3>Area of the image: </h3>" + str(height*width) + \
                   "<h3>Color: </h3>" + y + ", " + x

    return response


if __name__ == '__main__':
    app.run()