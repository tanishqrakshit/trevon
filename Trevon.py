from gtts import gTTS
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyaudio
import requests
import re
from weather import Weather

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Tanishq!")
        speak("Good Morning Tanishq!")

    elif hour>=12 and hour<18:
        print("Good Afternoon Tanishq!")
        speak("Good Afternoon Tanishq!")

    else:
        print("Good Evening Tanishq!")
        speak("Good Evening Tanishq!")

    print("I am Trevon. Hope you are doing well and how may I help you")
    speak("I am Trevon. Hope you are doing well and how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone( sample_rate=48000 ) as source:
        print("Speak now...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rakshittanishq@gmail.com', 'brickshere')
    server.sendmail('rakshittanishq@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'facebook' in query:
            webbrowser.open("facebook.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'whatsapp' in query:
            codePath = "C:\\Users\\TanishqRakshit\\Desktop\\WhatsApp.lnk"
            os.startfile(codePath)

        elif 'what\'s going on' in query:
            speak('Just talking to you')

        elif 'bye' in query or 'quit' in query:
            speak('Bye Tanishq! Have a nice day')
            break

        elif 'joke' in query:
            res = requests.get(
               'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
            if res.status_code == requests.codes.ok:
                print(str(res.json()['joke']))
                speak(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')

        elif 'funny' in query:
            speak('I know, sometimes I am too sarcastic')

        elif 'hello' in query:
            speak('Hello Tanishq!')

        elif 'trevon' in query:
            speak('Yes Tanishq?')

        elif 'email to myself' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "tanishq.rakshit@gmail.com"
                sendEmail(to, content)
                print("Sir, the mail has been sent successfully!")
                speak("Sir, the mail has been sent successfully!")
            except Exception as e:
                #print(e)
                print("Sorry tanishq. I am not able to send this email")
                speak("Sorry tanishq. I am not able to send this email")
