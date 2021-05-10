import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests


print('Lancement de ADA')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
   engine.say(text)
   engine.runAndWait()

def wishMe():
   hour=datetime.datetime.now().hour
   if hour>=0 and hour<12:
       speak("Bonjour Simon")
       print("Bonjour Simon")
   elif hour>=12 and hour<18:
       speak("Bonne après midi Simon")
       print("Bonne après midi Simon")
   else:
       speak("Bonsoir Simon")
       print("Bonsoir Simon")

def takeCommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
       print("J'écoute...")
       audio=r.listen(source)

       try:
           statement=r.recognize_google(audio,language='fr')
           print(f"user said:{statement}\n")

       except Exception as e:
           speak("Veuillez répéter, je n'ai pas bien compris")
           return "None"
       return statement

speak("Lancement de ADA")
wishMe()


if __name__=='__main__':


   while True:
       speak("Que puis-je faire pour vous ?")
       statement = takeCommand().lower()
       if statement==0:
           continue


       elif 'encyclopédie' in statement:
           wikipedia.set_lang('fr')
           speak('Je lance une recherche sur Wikipédia...')
           statement =statement.replace("Wikipédia", "")
           results = wikipedia.summary(statement, sentences=2)
           speak("Selon Wikipédia")
           print(results)
           speak(results)

       elif 'ouvre youtube' in statement:
           webbrowser.open_new_tab("https://www.youtube.com")
           speak("youtube s'ouvre dès maintenant")
           time.sleep(5)

       elif 'ouvre google' in statement:
           webbrowser.open_new_tab("https://www.google.com")
           speak("Google chrome s'ouvre dès maintenant")
           time.sleep(5)

       elif 'ouvre gmail' in statement:
           webbrowser.open_new_tab("gmail.com")
           speak("Gmail s'ouvre dès maintenant")
           time.sleep(5)

       elif "météo" in statement:
           api_key="1d4bdf7bf6a8d281e1cb58366ca4c6f4"
           base_url="https://api.openweathermap.org/data/2.5/weather?"
           speak("quelle est le nom de votre ville")
           city_name=takeCommand()
           complete_url=base_url+"appid="+api_key+"&q="+city_name
           response = requests.get(complete_url)
           x=response.json()
           if x["cod"]!="404":
               y=x["main"]
               current_temperature = y["temp"]
               temperature = round(current_temperature - 273.15)
               current_humidiy = y["humidity"]
               z = x["weather"]
               weather_description = z[0]["description"]
               speak("Aujourd'hui, attendez vous à  " +
                     str(weather_description) + " pour température de  " + str(temperature) + "degrés"+" et un pourcentage d'humidité de " +str(current_humidiy) +"%")
               print(" Temperature in kelvin unit = " +
                     str(current_temperature) +
                     "\n humidity (in percentage) = " +
                     str(current_humidiy) +
                     "\n description = " +
                     str(weather_description))

           else:
               speak(" La ville n'a pas été trouvée ")



       elif 'heure' in statement:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"il est  {strTime}")

       elif 'qui es-tu' in statement or 'que peux-tu faire' in statement:
           speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                 'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                 'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


       elif "qui t'as fabriqué" in statement or "qui t'as crée" in statement or "qui t'a conçu" in statement:
           speak("J'ai été conçu par le génie du mal, l'être le plus maléfique de la Terre")
           print("J'ai été conçu par Simon")

       elif "ouvre stackoverflow" in statement:
           webbrowser.open_new_tab("https://stackoverflow.com/login")
           speak("voici stackoverflow")

       elif "ouvre github" in statement:
           webbrowser.open_new_tab("https:/github/.com")
           speak("voici github")

       elif 'actualités' in statement:
           news = webbrowser.open_new_tab("https://www.lemonde.fr/")
           speak("J'ouvre dès maintenant Le Monde, bonne lecture ")
           time.sleep(6)

       elif "caméra" in statement or "prends une photo" in statement:
           ec.capture(0,"robo camera","img.jpg")

       elif 'recherche'  in statement:
           statement = statement.replace("recherche", "")
           webbrowser.open_new_tab(statement)
           time.sleep(5)

       elif 'je peux te poser une question' in statement:
           speak('Je peux répondre à des questions informatiques et géographiques, quelle question voulez vous me poser ?')
           question=takeCommand()
           app_id="A78K4G-Y24P332J7L"
           client = wolframalpha.Client('A78K4G-Y24P332J7L')
           res = client.query(question)
           answer = next(res.results).text
           speak(answer)
           print(answer)


       elif "éteins mon pc" in statement:
           speak("Je vais éteindre votre PC dès maintenant, veillez à sauvegarder toute vos applications")
           subprocess.call(["shutdown", "/l"])

       elif "au revoir" in statement or "ok au revoir" in statement or "stop" in statement:
           speak('your personal assistant G-one is shutting down,Good bye')
           print('your personal assistant G-one is shutting down,Good bye')
           break

time.sleep(3)

