# Text to speech library
import pyttsx3

# date time linrary
import datetime

# speech recognition library
import speech_recognition as sr

# initializing the pyttsx3 
engine = pyttsx3.init()

def speak(audio):
    """ speak function take audio as string argument """
    engine.say(audio)
    engine.runAndWait()

def time():
    """ time function says time in 12 hours format """
    time = datetime.datetime.now().strftime("%I:%M:%S") # 12 hours time format
    speak("The current time is")
    speak(time)

def date():
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
    speak("Welcome Back Sir!")
    time()
    date()

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

takeCommandFromUser()