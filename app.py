import PIL.Image
import flask

from flask import Flask, request, send_file


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


@app.route("/img", methods=['GET', 'POST'])
def img():
    if request.args.get('type') == '1':
        filename = 'b.png'
        image = PIL.Image.open(filename)
        width, height = image.size
        x = width + height
    else:
        filename = 'b.png'
        image = PIL.Image.open(filename)
        width, height = image.size
        response = "<h3>Width: </h3>" + str(width) + "<h3>Height: </h3>" + str(height)

    return response


if __name__ == '__main__':
    app.run()