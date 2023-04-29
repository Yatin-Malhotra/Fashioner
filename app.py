from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":

        
        files = request.files.getlist('files[]')
        file_names = []
        for file in files:
            filename = file.filename
            file_names.append(filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        return render_template('index.html', filenames=file_names)
        
        

    return render_template('index.html')
       



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)
