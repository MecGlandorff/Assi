# Lanugage model module, make sure you have a working OPENAI API key
# !pip install openai!: if you want to use this module separately

import openai


openai.api_key = "here"

def get_answer(question):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Use the chat model name
        messages=[{"role": "user", "content": question}]
    )
    answer = response['choices'][0]['message']['content']
    return answer

# Example usage
print(get_answer("What is the weather like?"))
