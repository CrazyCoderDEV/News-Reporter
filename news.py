import pyttsx3
import speech_recognition as sr
import requests
import json

class Reporter:

    @staticmethod
    def speak(audio):
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty('voices', voices[0].id)
        engine.say(audio)
        engine.runAndWait()

def get_user_voice():
    r = sr.Recognizer()
    with sr.Microphone() as input:
        audio = r.listen(input)

        try:
            voice_user = r.recognize_google(audio, language="en-us")
            print(f"Boss said:{voice_user}")


        except Exception as e:
            print(f"Exception: {str(e)}")

    return voice_user

if __name__ == "__main__":
    voice_user = get_user_voice().lower()

    url = ("http://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR API KEY HERE") # Put your API key here
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']

    a = 1
    n = 10

    if "start" in voice_user:
        Reporter.speak("Today's news articles are...")
        for article in articles:
            print(article['title'])
            Reporter.speak(article['title'])
            if a == n:
                break
            else:
                Reporter.speak("Moving on to the next article.")
                a += 1
                continue