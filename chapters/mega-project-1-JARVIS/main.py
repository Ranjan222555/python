import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',140)
newsapi= "dbc85f31777247348b5438cbb9cac9a2"



def speak(text):
    engine.say(text)
    engine.runAndWait()
  
def processcomand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")  
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")    
    elif "play" in c.lower():
        song =c.lower().split(" ")[1]
        link = musicLibrary.music[song]     
        webbrowser.open(link)  
    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code ==200:
            data = r.json()   # prase the json responce
            # extract article
            articles = data.get("articles", [])
            # print the headlines
            for article in articles:
                speak(article["title"])
               
if __name__ == "__main__":
    speak("initializing Jarvis for you ...")
    while True:
        # listen of the wake word "Jarvis"
        # obtain audio from the microphone
        r= sr.Recognizer()
        
        # recognize speech 
        print("recognizing.....")
        try:
            with sr.Microphone() as source:
                print("listening.....")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
                word =r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Yes i am here")
            # listen for  command
            with sr.Microphone() as source:
                print("Jarvis Active.....")
                audio = r.listen(source)
                command =r.recognize_google(audio)
                print(f"you said: {command}")
            processcomand(command)
            
        except Exception as e:
            print("error:".format(e))
              
    
    

