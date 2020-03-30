from flask import render_template

import app


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    return render_template("public/upload_image.html")