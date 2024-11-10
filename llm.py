# Lanugage model module, make sure you have a working OPENAI API key
# !pip install openai!: if you want to use this module separately

import openai

openai.api_key = ""

def get_answer(input):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=input,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Test debug line(s) below

# get_answer("What is the weather like?")