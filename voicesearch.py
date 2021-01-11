import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():    
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source) 
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command


def run():
    command = take_command()
    if 'play' in command:
        command = command.replace('play', '')
        talk('playing' + command)
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is ' + time)
        print(time)

run()