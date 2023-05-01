# Import Required Libraries
import tensorflow as tf
import os
from PIL import Image
import numpy as np
import ssl
from colorthief import ColorThief
from webcolors import CSS3_HEX_TO_NAMES as css3_hex_to_names
from scipy.spatial import KDTree

# Make the ssl unverified to prevent any licensing issues
ssl._create_default_https_context = ssl._create_unverified_context

# Load the VGG-16 pre-trained model
model = tf.keras.applications.vgg16.VGG16(include_top=True, weights='imagenet')

# Preprocess the image using the VGG-16 pre-trained model
def preprocess_image(image):
    input_shape = model.input_shape[1:3]

    resized_image = image.resize(input_shape)

    array_image = np.array(resized_image)

    expanded_image = np.expand_dims(array_image, axis=0)

    preprocessed_image = tf.keras.applications.vgg16.preprocess_input(expanded_image)

    return preprocessed_image

# Convert a color in hexadecimal representation to its RGB representation
def hex_to_rgb(hex_color):
    hex_color = hex_color.strip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return (r, g, b)

# Convert the RBG to a name
def convert_rgb_to_names(rgb_tuple):
    css3_db = css3_hex_to_names
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(np.array(rgb_tuple).reshape(1,-1))
    return names[index[0]]

# Get the most dominant color in the image
def get_dominant_color(image_path):
    color_thief = ColorThief(image_path)
    dominant_color = color_thief.get_color(quality=1)
    return dominant_color

# Classifies the clothes present in the image to a particular type
def classifier(image):
    try:
        preprocessed_image = preprocess_image(image)
        predictions = model.predict(preprocessed_image)
        class_label = tf.keras.applications.vgg16.decode_predictions(predictions, top=1)[0][0][1]
        return class_label
    except:
        return None

# Split the images into parts and classify them
# Returns a string array
def separator(images):
    classified_images = []
    counter = 0
    for image in images:
        filename = image.filename
        dominant_color = get_dominant_color(filename)
        class_label = classifier(image)
        if class_label is not None:
            color_name = convert_rgb_to_names(dominant_color)
            classified_image_with_color = color_name + "_" + class_label
            os.rename(filename, f"static/{classified_image_with_color}.jpg")
            classified_images.append(classified_image_with_color)
        counter += 1
    return classified_images
