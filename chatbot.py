from tkinter import *
import pyttsx3
import datetime
import AppOpener as Apk
import webbrowser
import pyautogui
import pywhatkit
import wikipedia

softs = [["google","Google Chrome"],["settings","Settings"],["vs code","Code"],["spotify","Spotify"],["chess","3D Chess Game"],["calculator","Calculator"],["calendar","Calendar"],["camera","Camera"],["clock","Clock"],["figma","Figma"],["sublime text","Submlime Text"],["my sql","mysql command line client"],["cmd","command prompt"],["python","pycharm community"],["github","Github "]] 

def speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
def wiki(query):
    try:
        # Search Wikipedia for the query
        search_results = wikipedia.search(query)
        if not search_results:
            speak("Sorry, I couldn't find any information on that.")
            return
        page = wikipedia.page(search_results[0])

        # Fetch and speak the summary
        summary = wikipedia.summary(search_results[0], sentences=5)
        print(summary)
        speak(summary)

    except wikipedia.exceptions.DisambiguationError as e:
        speak("Can you please be more specific?")
        print("DisambiguationError:", e)

    except wikipedia.exceptions.PageError as e:
        speak("Sorry, I couldn't find any information on that.")
        print("PageError:", e)

    except Exception as e:
        speak("Sorry, something went wrong.")
        print("Error:", e)


cb = Tk()
cb.title("ChatBot")
cb.geometry('600x600')
cb.config(bg='#0084ff')

xi = 0
yi = 0
def send_message():
    
    global yi
    u = user_entery.get()
    user = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='black', text=u+" < YOU",font=12,anchor='e')
    user.place(x=xi,y = yi)
    if f"open {soft[0]}" in u.lower():
        for soft in softs:
            if f"open {soft[0]}" in u.lower():
                bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text=f"BOT >opening {soft[0]}",font=12,anchor='w')
                bot.place(x=xi,y = yi+25)
                speak(f"opening {soft[0]}")
                Apk.open(f'{soft[1]}')
    
    if 'hello' in u.lower():
        bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text="BOT > Hello",font=12,anchor='w')
        bot.place(x=xi,y = yi+25)
        speak("Hello")
    elif "date" in u.lower():
            today = datetime.date.today()
            bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text=f"BOT >Today's date:{today}",font=12,anchor='w')
            bot.place(x=xi,y = yi+25)
            speak(f"Today's date:{today}")
            
    elif "you" in u.lower():
        bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text=f"BOT >Current Time = {current_time}",font=12,anchor='w')
        bot.place(x=xi,y = yi+25)
        speak(f"I can not share my personal details with a normal user")
        speak("I can not share my personal details with a normal user")
            
    elif "time" in u.lower():
        time = datetime.datetime.now()
        current_time = time.strftime("%H:%M:%S")
        bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text=f"BOT >Current Time = {current_time}",font=12,anchor='w')
        bot.place(x=xi,y = yi+25)
        speak(f"Current Time = {current_time}")
        
    
            
    elif "search" in u.lower():
        bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text="BOT >This is what I found on google",font=12,anchor='w')
        bot.place(x=xi,y = yi+25)
        url = f"https://www.google.com/search?q={u}"
        webbrowser.open(url)
        speak("This is what I found on google")
            
    elif "play" in u.lower():
        bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text=f"BOT >Playing song: {u[4:]}",font=12,anchor='w')
        bot.place(x=xi, y=yi+25)
        pywhatkit.playonyt(u)
        pyautogui.hotkey("k")
        speak(f"Playing song: {u[4:]}")
                    
    elif "close" in u.lower():
        bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text=f"BOT >Closing this window",font=12,anchor='w')
        bot.place(x=xi,y = yi+25)
        
        pyautogui.hotkey('alt', 'tab')
        pyautogui.hotkey('alt', 'f4')
        pyautogui.hotkey('enter')
        speak("Closing this window")
        
    if "explain" in u.lower():
            speak("speak the topic name again")
            print(f"topic : {u}")
            speak("connecing to server")
            wiki(u)      
    elif "stop" in u.lower():
        bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text=f"BOT >See you soon master",font=12,anchor='w')
        bot.place(x=xi,y = yi+25)
        speak("See you soon master")
        exit()    

    elif "scroll down" in u:
        bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text=f"BOT >scroled down",font=12,anchor='w')
        bot.place(x=xi,y = yi+25)
        pyautogui.scroll(100)
        speak("scroled down")
        
    elif "scroll up" in u:
        bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text=f"BOT >scroled up",font=12,anchor='w')
        bot.place(x=xi,y = yi+25)
        pyautogui.scroll(-100)
        speak("scrolled up")
            
            
            
            
            
            
            # More Functionality to be added
            
            


    else :
        bot = Label(chat_bg,height=1,width=64,bg = '#a6a6a6',fg='white', text="BOT > sorry i don't get you",font=12,anchor='w')
        bot.place(x=xi,y = yi+25)
    yi+=50
        
        
        
hcb_text= Label(height=2,width=14,bg='#0084ff',text='Desktop Assistant',font=('Times New Roman',20),fg='white')
hcb_text.place(x=200,y=5)

chat_bg = Frame(height=420,width=580,bg='#f5f5f5')
chat_bg.place(x=10,y=80)

entry_bg = Frame(height=60,width=500,bg='white')
entry_bg.place(x=10,y=520)

send_btn_bg = Frame(height=60,width=65,bg='white')
send_btn_bg.place(x=525,y=520)

def on_enter(e):
    user_entery.delete(0,'end')
    user_entery.config(fg='black')
def on_leave(e):
    text = user_entery.get()
    user_entery.config(fg='#5c5a5a')
    if text == "" or text == " ":
        user_entery.insert(0,'Enter Message......')
        user_entery.config(fg='#5c5a5a')

user_entery = Entry(entry_bg,width=32,bg='white',font=('Helvectica,20'), relief=FLAT,border=0)
user_entery.place(x=10,y=13)

user_entery.insert(0,'Enter Message......')
user_entery.config(fg='#5c5a5a')
user_entery.bind("<FocusIn>",on_enter)
user_entery.bind("<FocusOut>",on_leave)
sendBtn = Button(send_btn_bg,height=1,width=3,bg='#0084ff',text='>',font=('Helvectica',20),activeforeground='white',fg='white', relief=FLAT,border=0,activebackground='#0084ff',command=send_message)

sendBtn.place(x=5,y=5)
cb.mainloop()