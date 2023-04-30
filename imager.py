# Import Required Libraries
import requests
import json
import base64
from PIL import Image
from io import BytesIO

# Generate the Image
def generate_image(text):
    API_KEY = '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'

    prompt_text = f"A cartoon like outfit image for the following items {text} for a person"

    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        },
        data=json.dumps({
            "model": 'image-alpha-001',
            "prompt": prompt_text,
            "num_images": 1,
            "size": "512x512",
            "response_format": "url"
        })
    )

    try:
        image_url = response.json()["data"][0]["url"]
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image.save("static/outfit.jpeg")
    except KeyError:
        print("Error: data not found in API response.")
        image_url = None

######### TESTING BELOW ###########
generate_image("black_sweatshirt, whitesmoke_jean, lavender_jersey, wheat_running_shoe")
