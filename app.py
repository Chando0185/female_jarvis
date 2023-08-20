import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import sys
from elevenlabs import generate, play
from elevenlabs import set_api_key
set_api_key("Your API Key")

def engine_talk(query):
    audio = generate(
    text=query,
    voice="Grace", #Try with different voices too
    model="eleven_monolingual_v1"
    )

    play(audio)
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

# def engine_talk(text):
#     engine.say(text)
#     engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine_talk("Good Morning!")

    elif hour>=12 and hour<18:
        engine_talk("Good Afternoon!")   
        
    else:
        engine_talk("Good Evening!")  

    engine_talk("I am Female JARVIS Sir. You Can Call Me Alexa too, Please tell me how may I help you")  

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        print("Say that again please...")  
        return "None"
    return query
    
    
def run_alexa():
    command = takeCommand()
    if 'play' in command:
        song = command.replace('play', '')
        engine_talk('Playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' +time)
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        print(jokes)
        engine_talk(jokes+ "hahaha")
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('I could not hear you properly')
        
wishMe()       
while True:
    run_alexa()