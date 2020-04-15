from typing import io

import PIL.Image
import flask
import numpy
import os
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
    filename = request.files['file']
    image = PIL.Image.open(filename)
    width, height = image.size

    if request.args.get('type') == '1':
        response = width + height
    else:
        filename2 = secure_filename(filename.filename)
        # img = cv2.imread("01.jpeg", 1)
        # rgb = str(img.shape)
        # x=os.getcwd()

        for i in range(width):
            for j in range(height):
                r, g, b = image.getpixel((i, j))
                # rgb = str(image.shape)
                if r != g != b:
                    color = 'Color image'
                    year = '2019'
                else:
                    color = 'Grayscale image'
                    year = '1990'

        # img = cv2.imread('01.jpeg', 1) #1 means keep the img as it is, 0 converts to grayscale
        # if (len(img.shape) < 3):
        #     x = 'gray'
        #     y = str(img.shape)
        # elif len(img.shape) == 3:
        #     x = 'Color(RGB)'
        #     y = str(img.shape)
        # else:
        #     x = 'others'
        #     y = str(img.shape)

        response = "<h3>File name: </h3>" + filename2 + \
                   "<h3>Height & Width: </h3>" + str(height) + "px,  " + str(width) + "px" + \
                   "<h3>Color: </h3>" + color + \
                    "<h3>Year: </h3>" + year

    return response


if __name__ == '__main__':
    app.run()