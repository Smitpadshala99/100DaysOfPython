# For Mac
# from os import system
# names = ["Ram", "Shyam", "Lakhan"]
# for name in names:
#   system(f'say Shoutout to {name}')

import win32com.client as w

def pronounce_names(names):
    speaker = w.Dispatch("SAPI.SpVoice")
    
    # Loop through the names and pronounce each one
    for name in names:
        print(f"Shoutout to {name}")
        shoutout = f"Shoutout to {name}"
        speaker.Speak(shoutout)


l = ["Rahul", "Nishant", "Harry"]
pronounce_names(l)
