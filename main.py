import pywhatkit   
import speech_recognition as sr
import pyttsx3
import AppOpener as Apk
import webbrowser
import datetime
import pyautogui
r = sr.Recognizer()
def speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
def greet():
    x = datetime.datetime.now()
    h = int(x.strftime("%H"))
    if 3 < h < 12:
        speak("Good Morning master")
    elif 11 < h < 19:
        speak("Good AfterNoon Master")
    elif 18 < h < 22:
        speak("Good Evening master")
    elif 22 < h < 24:
        speak("it's late night master")
    else:
        speak("not a good time to work byy")
greet()  
softs = [["google","Google Chrome"],["settings","Settings"],["vs code","Code"],["spotify","Spotify"],["chess","3D Chess Game"],["calculator","Calculator"],["calendar","Calendar"],["camera","Camera"],["clock","Clock"],["figma","Figma"],["sublime text","Submlime Text"],["my sql","mysql command line client"],["cmd","command prompt"],["python","pycharm community"],["github","Github "]] 
softs = [["google","Google Chrome"],["settings","Settings"],["vs code","Code"],["spotify","Spotify"],["chess","3D Chess Game"],["calculator","Calculator"],["calendar","Calendar"],["camera","Camera"],["clock","Clock"],["figma","Figma"],["sublime text","Submlime Text"],["my sql","mysql command line client"],["cmd","command prompt"],["python","pycharm community"],["github","Github Desktop"]] 
while True:
    try:
        with sr.Microphone() as source:
            print("Listening........")
            audio = r.listen(source)
            print("Recognizing.......")
            MyText = r.recognize_google(audio, language='en-in')
            speak(f"command accepted{MyText}")
            # speak(f"executing {MyText}")
            
            if "date" in MyText.lower():
                today = datetime.date.today()
                speak(f"Today's date:{today}")
            
            if "you" in MyText.lower():
                speak("I can not share my personal details with a normal user")
            
            if "time" in MyText.lower():
                time = datetime.datetime.now()
                current_time = time.strftime("%H:%M:%S")
                speak(f"Current Time = {current_time}")

            for soft in softs:
                if f"open {soft[0]}" in MyText.lower():
                    Apk.open(f'{soft[1]}')
                    speak(f"opening {soft[0]}")

            if "search" in MyText.lower():
                google = MyText[14:]
                url = f"https://www.google.com/search?q={google}"
                webbrowser.open(url)
                speak("This is what I found on google")
            
            if "play" in MyText.lower():
                song = MyText[11:]
                print(f"Playing song: {song}")
                speak(f"Playing song: {song}")
                pywhatkit.playonyt(song)
                    
            if "close" in MyText.lower():
                pyautogui.hotkey('alt', 'f4')
                pyautogui.hotkey('enter')
                
            
            if "stop" in MyText.lower():
                speak("See you soon master")
                break
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")