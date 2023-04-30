from flask import Flask, render_template, request, url_for, redirect
import os
from classify import separator
from oufit import outfit_generator
from instructor import instructions
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'static/'

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":

        
        files = request.files.getlist('files[]')
        event = request.form['event']

        for file in files:
            name = file.filename
            file.save(os.path.join(UPLOAD_FOLDER, name))


        images = []
        for filename in os.listdir('static/'):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                img = Image.open(os.path.join(UPLOAD_FOLDER, filename))
                images.append(img)

        clothes = separator(images)

        print("Clothes:", clothes)

        
        outfits = outfit_generator(clothes, event)
        print("Outfits:", outfits)
        result = [s + ".jpg" for s in outfits]

        instructions_for_outfit = instructions(outfits)

        return render_template('outfit.html', outfits=result, instructions = instructions(outfits))
        
        

    return render_template('index.html')

@app.route('/reset', methods=["POST", "GET"])
def reset():
    # Iterate over all the files inside the folder
    for filename in os.listdir('static'):
        file_path = os.path.join('static', filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)

    return redirect(url_for('home'))
    #return render_template(url_for('reset'))

       



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)
