import openai

def instructions(output):
    openai.api_key = "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"
    
    # Set up the OpenAI API
    model_engine = "text-davinci-002"

    prompt = f"Give me a walkthrough on how to style these items: {output}"
    
    response = openai.Completion.create(        
        engine=model_engine,
        prompt=prompt,
        max_tokens=100
        )

    return response.choices[0].text