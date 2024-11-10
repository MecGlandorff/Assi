"""
This module is the text to speech module, which takes the response from the llm module and speaks it.
Also an idea to change of update this module so it can return text on screen as an answer. This is why it is named response.py"""

import pyttsx3

def speak(response_text):
    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()


# Testing lines for debugging below
speak("Hello, how can I help you?")