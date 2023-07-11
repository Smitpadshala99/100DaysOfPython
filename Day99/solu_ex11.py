import os
import time
import ctypes
import pyttsx3

REPEAT_INTERVAL = 3600  # Repeat frequency in seconds

# Initialize pyttsx3 speech engine
engine = pyttsx3.init()

while True:
    # Say the message
    engine.say("Hey Smit, Drink water")
    engine.runAndWait()

    # Display an alert dialog
    ctypes.windll.user32.MessageBoxW(0, "Hey Smit, Drink water", "Reminder", 1)

    time.sleep(REPEAT_INTERVAL)
