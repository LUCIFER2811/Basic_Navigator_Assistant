import datetime
import os
import random
import webbrowser

import pyttsx3
import speech_recognition as asap
import wikipedia

pa=random.randint(0,1)
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[pa].id)

# program for testing of speaking not used further
def sayit(audio):
    engine.say(audio)
    engine.runAndWait()
# function for speaking the correct time and wishing
if pa==0:
    s="jarvis"
    print("-----  --     --   -       - -------    ---")
    print("  |   /  \\    |  )  \\     /     |      |")
    print("  |  /----\\   | /    \\   /      |       ---")
    print("  | /      \\  | \\     \\ /       |          |")
    print("-- -        - |  \\     -     -------   ----")
else:
    s="friday"
    print(" ------ --   -------  ---        -- --   --")
    print(" |      |  )    |     |   \\     /  \\ \\  /")
    print(" |---   | /     |     |    |   / -- \\ \\/")
    print(" |      | \\     |     |    |  /      \\ \\ ")
    print(" |      |  \\    |     |   /  /        \\ \\")
    print("--      -  -- ------- ---   --        -- -")                    
sayit("establishing servers.....")
sayit("loading necessary data.....")
sayit("further decomposing.....")
sayit(f"hello sir i am{s}you personal assistant......I will help you in you different life chores and laptop activties and help you to do your work more efficiently and easier")

def time():
    timer=int(datetime.datetime.now().hour)
    minute=int(datetime.datetime.now().minute)
    if timer >=0 and timer<=12 :
        sayit(f"good morning sir the time is {timer} hours and {minute}minutes")
    elif timer>12 and timer<=18 :
        sayit(f"good noon sir the time is {timer} hours and {minute}minutes")
    else:
        sayit(f"good night sir the time is {timer} hours and {minute}minutes")
# function for recognizing the users voices
def acceptor():
    t=asap.Recognizer()
    with asap.Microphone() as source:
        print("Listening.......it")
        t.pause_threshold=0.9
        audio=t.listen(source)
        t.adjust_for_ambient_noise(source,duration=1)
    try :
        print("Recognizing.....it")
        prob=t.recognize_google(audio,language="hi-In")
        print(f"processing.....{prob}")
    except Exception :
        print("Sorry!please say it again...")
        return "nothing"
    return prob

# main function for execution
if __name__ == "__main__":
    while True:
        query=acceptor().lower()
        # function for searching
        if "wikipedia" in query:
            sayit("Searching it ........")
            query=query.replace("wikipedia","")
            found=wikipedia.summary(query,sentences=1)
            sayit(f"after searching from wikipedia i found this ...{found}")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")    
        elif "play music" in query:
            songs="C:\\music"
            music=os.listdir(songs)
            os.startfile(os.path.join(songs,music[random.randint(1,5)]))
        elif "time please" in query:
            time()
        elif "goodbye" in query :
            sayit("thank you sir i here buy end the program")
            print("Inisiating to end the program")
            break
        elif "open bluestacks" in query:
            # can assign any app
            path="C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(path)
        elif "open vs" in query:
            path1="C:\\Users\\theul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path1)
        
            
