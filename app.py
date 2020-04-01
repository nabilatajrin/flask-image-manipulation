import PIL.Image
import flask

from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

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
        response = "<h3>Width: </h3>" + str(width) + "<h3>Height: </h3>" + str(height) + "<h3>Area: </h3>" \
                   + str(height*width)

    return response


if __name__ == '__main__':
    app.run()