import speech_recognition as sr
import os
import sys
import openai
import google.generativeai as palm
import re

key = "AIzaSyC_TGXXzPQUWtjSkAJ9z-q4OasvdOAT4so"  # google api key

palm.configure(api_key=key)

quit_prog = False

def tts(message):
    if not isinstance(message, str):
        return ""
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak'
        return os.system(tts_engine + ' "' + message + '"')

# obtain audio from the microphone

# Example usage
text = "Hello, my name is Tina."

r = sr.Recognizer()
with sr.Microphone() as source:
    print("...")
    audio = r.listen(source)
# recognize speech using Google Speech Recognition
try:
    prompt = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said:\n " + prompt)

    response = palm.generate_text(prompt=prompt)
    tts(response.result)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



