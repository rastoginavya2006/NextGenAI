from datetime import datetime
import requests
import webbrowser
import speech_recognition as sr
import pyttsx3
current_time =datetime.now().time()

engine=pyttsx3.init()
engine.setProperty("rate",178)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        audio=rec.listen(source)
    try:
        query=rec.recognize_google(audio)
        print("You :",query)
        return query.lower()
    except :
        print("Can't catch that")
        return " "

greet_msgs=["hi","hello","hey","hi there","hello there"]
date_msgs=["date","tell me date","today's date"]
time_msgs=["time","tell me time","current time"]
news_msgs = ["tell me news", "news", "headlines"]
chat =True
def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=695e07af402f4b119f0703e9b19f4683"
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    for i in range(len(articles)):
        speak(articles[i]['title'])

while chat:
    #user_msg=input("Enter your message: ").lower()
    user_msg=listen()
    if user_msg in greet_msgs:
        print("Hello user. How may I help you ?")
       # speak("hello bachoo ")
    elif "open" in user_msg:
        website_name=user_msg.split()[-1]
        webbrowser.open(f"https://www.{website_name}.com")
    elif user_msg in news_msgs:
        get_news()
    elif user_msg in date_msgs:
        speak(f"Today's date is : {datetime.now().date()}")
    elif user_msg in time_msgs:
        print("Time is:",current_time.strftime("%I:%M:%S %p"))

    elif user_msg=="tata":
        chat=False
    else:
        print("I cannot understand")