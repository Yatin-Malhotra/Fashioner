import openai
import re

def outfit_generator(clothes, event):

    openai.api_key = "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"
    
    # Set up the OpenAI API
    model_engine = "text-davinci-002"
    
    prompt = f"in my closet, I have {clothes}. Make me just one outfit for a {event} with the items in my closet. At the end, can you just list the items used. At the end, can you just list the items used on separate lines using '-' at the beginning of each."
    
    
    #def generate_outfit():
    response = openai.Completion.create(        
        engine=model_engine,
        prompt=prompt,
        max_tokens=100
        )
    
    output = extract_lines(response.choices[0].text)
    print(output)
    print(concat_array(output))
    
    
def extract_lines(text):
    lines = text.split('\n')  # split the text into lines
    result = []  # create an empty array to store the lines starting with '-'

    for line in lines:
        if line.startswith('-'):
            result.append(line.strip('-').strip())  # remove the starting '-' and any leading/trailing whitespace, then add the line to the result array
        elif len(result) > 0 and not line.strip():  # if the line is blank (i.e. contains only whitespace characters) and at least one line has already been added to the result array
            break  # stop processing further lines

    return result



def concat_array(arr):
    # Join the array elements with a space in between
    concatenated_str = ', '.join(map(str, arr))
    return concatenated_str


#clothes = ["blue jeans", "white t-shirt", "black leather jacket", "red sneakers", "brown hoodie", "baggy pants", "violet blazer", "vest", "football jersey", "basketball shoes", "dress shoes", "chinos"]
# event = "wedding"

#outfit_generator(clothes, event)