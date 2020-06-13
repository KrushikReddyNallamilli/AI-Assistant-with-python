import pyttsx3
import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time=datetime.datetime.now().strftime("%I :%M: %S")
    speak(time)
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak("welcome back sir")
    speak("The current time is ")
    time()
    speak("The current date is")
    date()
    speak("Jarvis at your service. Please tell me how can I help you!sir")

wishme()