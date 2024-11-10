"""
This module is the text to speech module, which takes the response from the llm module and speaks it.
Also an idea to change of update this module so it can return text on screen as an answer. This is why it is named response.py"""

import pyttsx3

def speak(response_text):
    engine = pyttsx3.init()
    
    # Set properties for a more natural voice
    voices = engine.getProperty('voices')
    
    # Try a different voice (if available)
    for voice in voices:
        if "female" in voice.name.lower():  # Try to pick a female voice if available
            engine.setProperty('voice', voice.id)
            break
    else:
        engine.setProperty('voice', voices[0].id)  # Default to the first voice
    
    # Adjust the rate for smoother speech
    engine.setProperty('rate', 150)  # Adjust speed as per your preference
    
    # Adjust the volume if necessary
    engine.setProperty('volume', 0.9)  # 0.0 to 1.0
    
    # Speak the text
    engine.say(response_text)
    engine.runAndWait()

# Testing lines for debugging below
speak("It's 16 degrees outside")
