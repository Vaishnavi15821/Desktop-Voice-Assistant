from time import sleep, strftime
from cv2 import VideoCapture
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import json
import operator
import wolframalpha
import shutil
from ecapture import ecapture as ec
import winshell
import pyjokes
import cv2 as cv
import time
from urllib.request import urlopen
import requests
import subprocess
import smtplib

from plyer import notification

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
     speak("Good Morning!")

    elif hour>=12 and hour<=17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I'm David! How may i help you?")

def username():
    speak("What should i call you?")
    uname = takecommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    speak("How can I help you, "+uname)

#this func takes microphone i/p from user and returns string o/p
def takecommand():
   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1  # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)


    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-us')
        print("User said: ", query)

    except Exception as e:
        print(e)

        print("Say that again please:")
        return "None"
    
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('surabhipardeshi20@gmail.com', '###A1b2c3')
    server.sendmail('surabhipardeshi20@gmail.com', to, content)
    server.close()




if __name__== "__main__":
    
    
    
    while exit!=True:
        query=takecommand().lower()
        
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open coursera' in query:
            webbrowser.open("coursera.org/in")

        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'time' in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("The time is:",strfTime)
            speak(strfTime)

        elif 'open visual studio code' in query:
            path= "C:\\Users\\SURABHI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'open ms word' in query:
            path= "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path)

        elif 'open gmail' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = r"C:\Users\SURABHI\Desktop\New folder (2)\Gigakoops - Grinding Nemo.mp3"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'joke' in query:
            c=pyjokes.get_joke()
            print(c)
            speak(c)
        
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you?")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "camera" in query or "take a photo" in query:
            cap=cv.VideoCapture(0)
            ret,frame=cap.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            backtorgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            cv.imshow('captured image',backtorgb)
            cv.waitKey(5)
            cap.release()

 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query:
            speak("uhm uhm.")

    

        elif 'ask' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takecommand()
            app_id="TEK3YX-U9G63XVT3V"
            client = wolframalpha.Client('TEK3YX-U9G63XVT3V')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "wish me" in query:
            wishme()     
         
        elif "write a note" in query:
            speak("What should i write?")
            note = takecommand()
            file = open('jarvis.txt', 'w')
            speak("Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%M%p")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "current location" in query:
             ip_request = requests.get('https://get.geojs.io/v1/ip.json')
             my_ip = ip_request.json()['ip']
             geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
             geo_data = geo_request.json()
             geo = geo_data['city']
            
             speak("You are in"+geo)
             print("You are in "+geo)
             speak("Your detailed location and timezone is displayed below: ")
             print(geo_data)
            
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
        
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takecommand())
            time.sleep(a)
            print(a)

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])   
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
    
        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "surabhi.pardeshi@cumminscollege.in"   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif "set reminder" in query:
           speak("What should i say?")
           msg=takecommand()
           speak("Set time")
           t=takecommand()

           notification.notify(title = "REMINDER", message=msg,timeout=2)

        elif "weather" in query:
            api_key="ede647f8f0454190970172613222905"
            base_url="https://www.weatherapi.com/"
            speak("what is the city name")
            city_name=takecommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))