# Write a program to pronounce list of names using win32 API.

import win32com.client as w

def pronounce(names):
    speaker = w.Dispatch("SAPI.SpVoice")

    for name in names:
        print("Shoutout to "+name)
        speaker.Speak("Shoutout to " + name)
    speaker.Speak("Thank You So Much!")

l = ["Ram", "Lakhan", "Hanuman", "Smit", "ALL"]
pronounce(l)