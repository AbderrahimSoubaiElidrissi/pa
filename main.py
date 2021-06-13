import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', "english_rp+f3")

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


def listen():
    r = sr.Recognizer()  # Creating a recognizer object

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:  # Checking for unknown errors
        print('Google Speech Recognition could not understand the audio')
    except sr.RequestError as c:
        print('Request results from Google Speech Recognition service error')

    return data

def greeting(text):
    Greeting_Inputs = ['hi', 'hey','hello']
    for word in text.split():
        if word.lower() in Greeting_Inputs:
            return "Hello dear"
    return ''

def goodbye(text):
    Greeting_Inputs = ['good bye', 'ok bye','stop']
    for word in text.split():
        if word.lower() in Greeting_Inputs:
            return "Shutting down,Good bye"
    return ''

def log(text):
    print("LOG: "+ text)


log('LOG: Booting personal assistant')

while True:
    text = listen()
    responses = ''

    if text == '': 
        continue
    elif greeting(text) != '':
        log('Greeting')
        responses = greeting(text)

    elif goodbye(text) != '':
        log('Shutting down')
        responses = goodbye(text)
        
    elif 'date' in text:
        log('Getting date')
        get_date = getDate()
        responses = responses + ' ' + get_date
    elif responses != '':
        responses = responses + "I'm Sorry I Can't Do That Yet"

    say(responses)