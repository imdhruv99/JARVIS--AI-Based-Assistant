# Text to speech library
import pyttsx3

# date time linrary
import datetime

# speech recognition library
import speech_recognition as sr

# wikipedia library
import wikipedia as wiki

# email library
import smtplib

# web browser library
import webbrowser as wb

# Laptop CPU and Battery Status
import psutil

# jokes library
import pyjokes

# operating system library
import os

# gui library
import pyautogui

# random library
import random

# json library
import json

# http request library
import requests

# url library
from urllib.request import urlopen

# calculation library
import wolframalpha as wfa

# time library
import time

# initializing the pyttsx3 
engine = pyttsx3.init()

wfa_app_id = 'L87GUQ-RRUEE79WT5'

def speak(audio):
    """ speak function take audio as string argument """
    engine.say(audio)
    engine.runAndWait()

def time_():
    """ time function says time in 12 hours format """
    timeRes = datetime.datetime.now().strftime("%I:%M:%S") # 12 hours time format
    speak("The current time is")
    speak(timeRes)

def date_():
    """ date funtion says date in date/month/year format """
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishMe():
    """ wishMe function greet us everytime we start the application and say current date and time """
    speak("Welcome Back,")
    # time()
    # date()

    # adding more greeting statements to make it more pleasing and appealing
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    
    speak("Jarvis at your service, how can i help you today?")


def takeCommandFromUser():
    """ takeCommandFromUser will take speech from user """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1 # how much time it will wait for user
        audio = r.listen(source) # whatever it listen, it will store in audio
    
    try:
        print("Recognizing.....")
        
        # command given by user will be stored in query
        query = r.recognize_google(audio, language='en-US')
        print(query)
    
    except Exception as e:
        print(e)
        print("please, say again.....")
        return "None"
    
    return query

def sendEmail(to, content):
    """ sendEmail function use to send email, It takes to argument `to = receiver's email` and `content = content of email` """

    server = smtplib.SMTP('smtp.gmail.com', 587)
    # ehlo function help us to identifying our self to esmt server
    server.ehlo()
    server.starttls()

    # for jarvis being able to send email, we must enable low security setting in our gmail account
    # update your email and password below
    server.login('emailAddress@gmail.com', 'password@123')
    server.sendmail('emailAddress@gmail.com', to, content)
    server.close()


def cpu():
    """ cpu function will give us infromation about cpu """

    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)

def battery():
    """ Battery Function will give us information about battery """

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged:
        speak("Battery is plugged in and battery percent is")
        speak(percent)
    else:
        speak("Battery percent is")
        speak(percent)

def joke():
    """ joke function will tell us jokes """

    speak(pyjokes.get_joke())

def offline():
    """ Simple offline function """
    quit()

def screenShot():
    img = pyautogui.screenshot()
    img.save('E:/Photos and Videos/My Photos/screenshot.png')

if __name__ == "__main__":

    # calling wish me function everytime jarvis wakes up
    wishMe()

    while True:

        # all the command will be stored in lower case in query
        query  = takeCommandFromUser().lower()

        # tell us time when asked
        if 'time' in query:
            time_()
        
        # tell us time when asked
        if 'date' in query:
            date_()
        
        elif 'wikipedia' in query:
            speak('Searching....')

            # replacing wikipedia
            query = query.replace('wikipedia', '')
            
            # getting result of wikipedia search, return and speak first 3 line of search
            result = wiki.summary(query, sentences = 3)
            speak('According to Wikipedia')

            # printing and speaking the result
            print(result)
            speak(result)
        
        elif 'send email' in query:
            
            try:

                # storing each sentence of user in content
                speak('sir, what do you want to say?')
                content = takeCommandFromUser()

                # provide reciever email address
                speak("please provide me receiver's email adress")
                receiver = input("Please, Enter the receiver's email address:")
                to = receiver

                # sending email
                sendEmail(to, content)

                # speaking what i have said to send in email, just for cross verification
                speak(content)

                speak("Email has been sent succesfully")
            
            except Exception as e:
                print(e)
                speak("Sorry, Unable to send Email.")

        elif 'search in chrome' in query:

            speak("Please say me what shoud I seach?")

            # path of application install location
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            # search string 
            search = takeCommandFromUser().lower()
            wb.get(chromepath).open_new_tab(search)
        
        elif 'search in youtube' in query:
            
            speak("Please say me what shoud I seach?")

            # search string
            searchTerm = takeCommandFromUser().lower()
            speak("Here we go to YouTube!")

            # searching on youtube
            wb.open('https://www.youtube.com/results?search_query=' + searchTerm)

        elif 'search in google' in query:
            
            speak("Please say me what shoud I seach?")

            # search string
            searchTerm = takeCommandFromUser().lower()
            speak("Searching.....")

            # searching on google
            wb.open('https://www.google.com/search?q=' + searchTerm)
        
        elif 'cpu' in query:
            cpu()
        
        elif 'battery' in query:
            battery()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak('Going offline Sir!')
            offline()

        elif 'notepad' in query:
            """ it is static as of now, i am searching for make it dynamic for each apps """
            speak("Opening Notepad.....")
            notepad = r'C:\Windows\System32\notepad.exe'
            os.startfile(notepad)
        
        # writing notes
        elif 'write a note' in query:
            speak('What should I write, Sir?')
            # getting sentences from user
            notes = takeCommandFromUser().lower()
            file = open('note.txt', 'w')
            # asking for Date and Time
            speak("Sir, should I include Date and Time?")
            ans = takeCommandFromUser().lower()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done Taking Notes, Sir!")
            else:
                file.write(notes)
        
        # Speaking and reading Notes
        elif 'show note' in query:
            speak("Showing Notes")
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())
        
        elif 'screenshot' in query:
            speak("Taking Screenshot Sir!")
            screenShot()
            speak("Sir, Screenshot has been taken.")
        
        elif 'play music' in query:
            songsDir = 'path to the location'
            # listing all the song available in directory
            music = os.listdir(songsDir)
            speak('Which song song should I play?')
            speak('select a number.....')
            ans = takeCommandFromUser().lower()

            while 'number' not in ans and ans != 'random' and ans!= 'you choose':
                speak('I could not understand you, Please Try again.')
                ans = takeCommandFromUser().lower()

            if 'number' in ans:
                # replacing integer value with number
                no = int(ans.replace('number', ''))
            
            if 'random' or 'you choose' in ans:
                no = random.randint(1, 100)
            
            # joining the songs directory with no of song
            os.startfile(os.path.join(songsDir, music[no]))

        # remeber that
        elif 'remember that' in query:
            speak("What should I remeber?")
            memory = takeCommandFromUser()
            speak("You asked me to remember that" + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt', 'r')
            speak("You asked me to remember that" + remember.read())

        # news 
        elif 'news' in query:
            try:
            
                # wallstreet news api
                jsonObject = urlopen("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=0cb8c1a6fc924e2e981077306a7336f3")
                # loading json data
                data = json.load(jsonObject)
                i = 1
                speak("Here are some top headlines from wall street news.....")
                print('===========================TOP HEADLINES==========================='+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+ item['title']+ '\n')
                    print(item['description'] + '\n')
                    speak(item['title'])
                    i += 1
            
            except Exception as e:
                print(str(e))
        
        elif 'where is' in query:
            # replacing where is string, so code can understand the place or location name
            query = query.replace("where is", "")
            location = query
            speak("User asked to locate" + location)
            # open new tab from web browser library
            wb.open_new_tab("https://www.google.com/maps/place/" + location)
        
        # calculate
        elif 'calculate' in query:
            client = wfa.Client(wfa_app_id)
            # extracting index from query by splitting
            index = query.lower().split().index('calculate')
            query = query.split()[index + 1:]
            result = client.query(''.join(query))
            answer = next(result.results).text
            print("The answer is:" + answer)
            speak("The answer is" + answer)

        # explaining words
        elif 'what is' in query or 'who is' in query:
            # using the same API
            client = wfa.Client(wfa_app_id)
            result = client.query(query)

            try:
                print(next(result.results).text)
                speak(next(result.results).text)
            except StopIteration:
                print("No Results")
        
        # stop listening 
        elif 'stop listening' in query:
            speak('For how many second you want me to stop listening to your commands?')
            ans = int(takeCommandFromUser())
            time.sleep(ans)
            print(ans)

        # using below jarvis can control logout, restart and shutdown
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

#################################################
#                                               #
#  To make exe type below command in terminal   #
#  pyinstaller --onefile  main.py               #
#                                               #
#################################################