"""
Main and keyboard module in one. Not so neat maybe but does the job
"""

# Required pips: pip install keyboard

import keyboard
from speech_recognition import listen
from llm import get_answer
from response import speak

def main():
    input = listen()
    if input == True:
        answer = get_answer(input)
        speak(answer)

# Keyboard key for activating Assi assistent. So press ctrl, shift and space to run it while running main.py
keyboard.add_hotkey('ctrl+shift+space', main)

