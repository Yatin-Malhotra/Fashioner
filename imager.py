# Import Required Libraries
import requests
import json
import base64
from PIL import Image
from io import BytesIO

# Generate the Image
def generate_image(text, gender, race):
    API_KEY = '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'

    prompt_text = f"A cartoon like image for a fashionable outfit using only the following items {text} for a {race} {gender}"

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
        image.save(f"outfit.jpeg")
    except KeyError:
        print("Error: data not found in API response.")
        image_url = None

######### TESTING BELOW ###########
generate_image("blue jeans, white t-shirt, black leather jacket, red sneakers", "man", "brown")