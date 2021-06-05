import pyttsx3

text = "welcome to python"
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()