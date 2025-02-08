# use import so that we can write it in short form
import speech_recognition as sr
import webbrowser
import pyttsx3 #converts text to speech
import musiclibrary
import requests

recognizer = sr.Recognizer() #recognizes what the user speaks
engine = pyttsx3.init()
newsapi = "1ab8a00aad8340c38c1fd264206c3d86"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    elif command.lower() .startswith("play"):
        song = command.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "open spotify" in command.lower():
        webbrowser.open("https://spotify.com")
    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

        # Parse the JSON response
        data = r.json()
    
    # Check if the response contains articles
    if data.get("status") == "ok" and "articles" in data:
        articles = data["articles"]
        
        # Print each headline
        speak("Top Headlines from the world:")
        for i, article in enumerate(articles, start=1):
            speak(f"{i}. {article.get('title', 'No Title')}")
        

if __name__ == "__main__": # use "__name__ == "__main__" to let the program directly through scripts
    speak("Hello Mother fucker....")
    while True:
        # listen for the wake word "Jarvis"
        # timeout is used to limit the time for execution
       r = sr.Recognizer()
       print("recognizing....")
       try:
           with sr.Microphone() as source: 
               print("Say something!")
               audio = r.listen(source, timeout=4, phrase_time_limit=2)
           word = r.recognize_google(audio)
           if (word.lower() == "jarvis"):
                speak("Yes bitch??")
                # listening for command
                with sr.Microphone() as source:
                  print("Jarvis Active")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)
                  speak("Sure")
                  

                  processcommand(command)
       
       except Exception as e:
            print("Error!!!; {0}".format(e))
