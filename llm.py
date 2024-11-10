# Lanugage model module, make sure you have a working OPENAI API key
# !pip install openai!: if you want to use this module separately

import openai

openai.api_key = "YOUR_API_KEY"

def get_answer(input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Test debug line(s) below

get_answer("What is the weather like?")