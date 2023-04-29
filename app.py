from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import os
from classify import separator
from oufit import outfit_generator
from imager import generate_image
from PIL import Image

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":

        
        files = request.files.getlist('files[]')
        event = request.form['event']

        for file in files:
            name = file.filename
            file.save(os.path.join('static/input', name))

        images = []
        for filename in os.listdir('static/input'):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                img = Image.open(os.path.join('static/input', filename))
                images.append(img)

        clothes = separator(images)

        
        outfit = outfit_generator(clothes, event)
        generate_image(outfit, "male", "white")

        return render_template('index.html', outfit=True)
        
        

    return render_template('index.html')
       



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)
