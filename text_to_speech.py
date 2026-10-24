import pyttsx3                      # importing library

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()

# text_to_speech("hello world")