import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from gtts import gTTS
import pygame
import os
recognizer=sr.Recognizer()

def speak_old(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

pygame.mixer.init()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')


    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()


    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def prossesscommand(c):
    if "open youtube" in c.lower():
          speak("opening youtube")
          webbrowser.open("https://youtube.com")
    elif "open google" in c.lower():
         speak("opening google")
         webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
         speak ("opening facebook")
         webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
         speak("opening linkedin")
         webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
         webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]

        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            speak("playing " + song)
            webbrowser.open(link)
        else:
            speak("song not found")

   
if __name__=="__main__":
    speak(" initializing  Friday.....")

    while True:       
        print("Reconizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = recognizer.listen(source,timeout=5,phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if "friday" in word.lower():
                speak("yes")
            

                with sr.Microphone() as source:
                        print("Friday active")
                        audio = recognizer.listen(source)
                command=recognizer.recognize_google(audio)
                prossesscommand(command)

            
                
            
        except Exception as e:
            print("Error:{0}".format(e))

           
           