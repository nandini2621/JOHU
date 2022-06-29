import pyttsx3 #text to speech conversion
import datetime 
import speech_recognition as sr #uses microphones require PyAudio
import wikipedia
import webbrowser
import subprocess #Connect to the new process & obtain their output 
import wolframalpha #API which computes answering through wolfram's algorithms and AI technology

engine = pyttsx3.init('sapi5') #Microsoft speech API for voice recognition
voices = engine.getProperty('voices') #voice id male or female voice
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
        engine.say(audio)
        engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour) #to get curent month,date,year,hour,min,sec -> print(now.hour,now.year)
        if hour>=00 and hour<12:
                speak("good morning")
        elif hour>=12 and hour<16:
                speak("good afternoon")
        else:
                speak("good evening")
        if  __name__=="__main__":
                print("I am JOHU")
                speak ("I am JO HU.. i m invented to help you.... so How can i help you")
                
def johu(data):
    if "how are you" in data:
                speak("I am fine")

def takeCommand():
        r = sr.Recognizer()#recognize speech input
        with sr.Microphone() as source: #uses defalut microphone as audio source
                print("Try speaking...")
                speak("Try speaking...")
                r.pause_threshold = 1 #1 sec for no audio input or there is pause by user
                audio = r.listen(source) #listen to the first phrase and extract it into audio data

        try:
                print("Getting to you....")
                query = r.recognize_google(audio, language='en-in') #Recognize speech using GOogle speech Recognition
                print(f"User said: {query}\n")

        except :

                print("Say that again please or say stop/exit/bye to terminate JOHU...")
                return "None"
        return query

def search_google(query):
       print("What you want to search on Google")
       speak("What you want to search on google")
       r = sr.Recognizer()
       with sr.Microphone() as source:
               r.adjust_for_ambient_noise(source) #detects if there is background noise
               audio = r.listen(source)
               text=r.recognize_google(audio)
       print(text)
       speak("searching for")
       speak(text)
       url='https://www.google.com/search?q='
       search_url=url+text
       webbrowser.open(search_url) #to open web browser site
       return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if query==0:
            continue
            
        if "stop" in query or "exit" in query or "bye" in query:
            print("Ok bye!!! Thank you!! and Take care!!")
            speak("Ok bye!!! Thank you!! and Take care!!")
            break

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10) #from wikipedia(title=query by user, no. of sentences in answer)
            speak("According to Wikipedia,")
            print(results)
            speak(results)
            

        elif 'can you please open youtube' in query or 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")    

        elif 'can you please open cu website' in query or 'open CU website' in query or "open cuims" in query:
            speak("Opening chandigarh university management system")
            webbrowser.open("uimms.cuchd.in/uims/")    

        elif 'can you please open instagram' in query or 'open instagram' in query:
            speak("Opening instagram")
            webbrowser.open("instagram.com")    

        elif 'can you please open facebook' in query or 'open facebook' in query:
            speak("Opening facebook")
            webbrowser.open("facebook.com")   

        elif 'can you please open Amazon' in query or 'open Amazon' in query:
            webbrowser.open("amazon.in") 

        elif 'can you please open flipkart' in query or 'open flipkart' in query:
            speak("Opening flipkart")
            webbrowser.open("flipkart.com")    

        elif 'can you please open cars24' in query or 'open cars24' in query:
            webbrowser.open("cars24.com")   

        elif 'can you please open olx' in query or 'open olx' in query:
            speak("Opening olx")
            webbrowser.open("olx.in")    

        elif 'can you please open blackboard' in query or 'open blackboard' in query:
            webbrowser.open("eu.bbcollab.com")    

        elif 'can you please open hindustan times' in query or 'open hindustan times' in query:
            speak("Opening hindustan times")
            webbrowser.open("m.hindustantimes.com")    

        elif 'can you please open apple store' in query or 'open apple store' in query:
            speak("Opening apple store")
            webbrowser.open("apple.com")    

        elif 'can you please tell me the weather' in query or 'tell me the weather' in query:
            speak("Opening accuweather")
            webbrowser.open("accuweather.com")    

        elif 'can you please open spotify' in query or 'open spotify' in query:
            speak("Opening spotify")
            webbrowser.open("spotify.com")    
  
        elif "open chrome" in query or "can you please open chrome" in query or "open google chrome" in query:
             speak("Opening Google Chrome") 
             subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe') #getiing from the directory of the system
             
        elif "open microsoft edge" in query or "open edge" in query or "can you please open edge" in query: 
            speak("Opening Microsoft Edge") 
            subprocess.Popen('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe') 
  
        elif "open word" in query or "can you please open word" in query: 
            speak("Opening Microsoft Word") 
            subprocess.Popen('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs') 
            
        elif "open excel" in query or "can you please open excel" in query: 
            speak("Opening Microsoft Excel") 
            subprocess.Popen('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs')    

        elif "do my calculation" in query or "open calculator" in query or "calculate" in query:
            print("Enter your input for calculating")
            speak("enter your input for calculating")
            app_id = "J2YRR9-EHWQT8HPAQ"
            client = wolframalpha.Client(app_id)
            response = client.query(input()) #take audio input as query
            result = None
            for result in response.results: 
                  pass
            if result is not None:
                print(f"The answer is {result.text}".format(result.text)) #text output
                speak(f"The answer is {result.text}".format(result.text))
              
        elif "search on google" in query or "search" in query or 'search google' in query:
             search_google(query)

        elif "what's the time Johu" in query or "tell me the time" in query:
              strTime=datetime.datetime.now().strftime("%H:%M:%S") #strftime method returns a string representing date and time 
              print(f"The time is {strTime}")
              speak(f"The time is {strTime}")

        elif "how are you" in query:
             print("I am fine..what about you buddy")
             speak("I am fine..what about you buddy")
 
        elif "where do you live" in query:
            print("I am basically an AI assistant i am made via python programme..so i live in python programm.")
            speak("I am basically an AI assistant i am made via python programme..so i live in python programm.")
 
        elif "why you have been made" in query or "who made you" in query:
            print("Basically i was made as a project by my inventors Nandini,Rishabh,Faisal,Suraj")
            speak("Basically i was made as a project by my inventors Nandini,Rishabh,Faisal,Suraj")
 
        elif "who is faisal" in query or "who is suraj" in query or "who is rishab" in query or "who is nandini" in query:
            print("My Inventor's Name")
            speak("My Inventor's Name")
            
        elif "open notepad" in query or "can you please open notepad" in query:
             speak("Opening notepad")
             subprocess.Popen('%windir%\\system32\\notepad.exe')
             #from subprocess module popens opens pipe(method/func to pass information pass from one process to another) from input command 

        elif "restart the PC" in query or "restart" in query:
                subprocess.call(["shutdown", "/r"])

             

        
