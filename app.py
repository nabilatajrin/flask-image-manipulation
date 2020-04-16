import PIL.Image
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

# instantiate/ create the application
app = Flask(__name__)


# route, when someone calls the route the code associated with it will get run
# an app can handle multiple routs
# this is also an endpoint. an app can have multiple endpoints.
# home page
@app.route('/', methods=["GET", "POST"])
def home():
    return "Welcome to home page!"

# check whether an image is new or old based on logic if the image is color or grayscale.

# there could be different methods on it.
# method includes the type of requests it is getting sends over
# ['GET', 'POST'] means it will accept get request and post request.
@app.route("/img", methods=['GET', 'POST'])
def img():
    filename = request.files['file']
    username = request.form['username']
    image = PIL.Image.open(filename)
    width, height = image.size

    filename2 = filename.filename

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
                "<h3>Year: </h3>" + year + \
                "<h3>Username: </h3>" + username

    return response


# if I call the file directly from the command line I want to execute what follows here
if __name__ == '__main__':
    # run the app
    app.run()