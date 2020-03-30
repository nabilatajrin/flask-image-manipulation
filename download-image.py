from flask import Flask, request, send_file

download = Flask(__name__)

# download selected image and forward to processing page
@download.route("/download", methods=['GET', 'POST'])
def download():
    if request.args.get('type') == '1':
        filename = 'b.png'
    else:
        filename = 'b.png'
    return send_file(filename, mimetype='b/png')


if __name__ == '__main__':
    download.run()