import pyttsx3

def text_to_Speech(text):
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 'rate-80')
    engine.say(text)
    engine.runAndWait()

