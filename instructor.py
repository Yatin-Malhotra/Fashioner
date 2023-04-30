import openai

def instructions(output):
    openai.api_key = "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"
    
    # Set up the OpenAI API
    model_engine = "gpt-3.5-turbo"

    prompt = f"Give me a walkthrough on how to stylishly wear these clothing items: {output}"
    
    chatgpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=2000,
            top_p=0.95)

    response = chatgpt_response['choices'][0]['message']['content'].strip()

    index = response.index('1.')
    response = response[index:]
    print(response)
    return response
