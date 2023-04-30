import openai
import re

def outfit_generator(clothes, event):

    openai.api_key = "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"
    
    # Set up the OpenAI API
    model_engine = "gpt-3.5-turbo"
    
    prompt = f"in my closet, I have {clothes}. Make me just one outfit for a {event} with the items in my closet. At the end, can you just list the items used. At the end, can you just list the items used on separate lines using '-' at the beginning of each. Also do not repeat clothes of the same type or category (i.e. only give one footwear). Make sure there are at least some pants/jeans in each outfit."
    
    
    # #def generate_outfit():
    # response = openai.Completion.create(        
    #     engine=model_engine,
    #     prompt=prompt,
    #     max_tokens=100
    #     )
    
    # output = extract_lines(clothes,response.choices[0].text)
    # print("GPT Output", output)
    chatgpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=2000,
            top_p=0.95)

    response = chatgpt_response['choices'][0]['message']['content'].strip()

    print("Response:", response)

    output = extract_lines(clothes, response)
    print("GPT Output", output)
    return output
    
    
def extract_lines(clothes, text):
    lines = text.split('\n')  # split the text into lines
    result = []  # create an empty array to store the lines starting with '-'

    clothes_copy = []
    for cloth in clothes:
        stripped_cloth = (cloth.strip('-').strip().replace(" ", "_")).lower()
        clothes_copy.append(stripped_cloth)

    #print("Clothes:", clothes)
    #print("Clothes Copy:", clothes_copy)

    for line in lines:
        if line.startswith('-'):
            stripped_line = (line.strip('-').strip().replace(" ", "_")).lower()
            #print("Stripped Line:", stripped_line)
            for cloth in clothes_copy:
                #print("Cloth:", cloth)
                #print("Stripped Line:", stripped_line)
                if (stripped_line == cloth):
                    index = clothes_copy.index(line.strip('-').strip().replace(" ", "_").lower())
                    #print("Index:", index)
                    if clothes[index] not in result:
                        result.append(clothes[index])  # remove the starting '-' and any leading/trailing whitespace, then add the line to the result array
        elif len(result) > 0 and not line.strip():  # if the line is blank (i.e. contains only whitespace characters) and at least one line has already been added to the result array
            break  # stop processing further lines

    return result


# def concat_array(arr):
#     # Join the array elements with a space in between
#     concatenated_str = ', '.join(map(str, arr))
#     return concatenated_str


#clothes = ["blue jeans", "white t-shirt", "black leather jacket", "red sneakers", "brown hoodie", "baggy pants", "violet blazer", "vest", "football jersey", "basketball shoes", "dress shoes", "chinos"]
# event = "wedding"

#outfit_generator(clothes, event)
