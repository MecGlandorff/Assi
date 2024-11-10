# This is the speech recognition modules
# !pip install SpeechRecognition! This installs the google speech recog module. 

import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.recognize_google(source)
        
        try:
            input = recognizer.recognize_google(audio)
            print(f"Command = {input}")
            return input.lower()
        
        except sr.UnknownValueError:
            print("Didn't catch that")
            return None