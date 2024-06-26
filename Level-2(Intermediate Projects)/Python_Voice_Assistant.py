Python Voice Assistant



Features:
*Speech recognition: Uses Google Speech Recognition to convert your spoken commands to text.
*Text-to-speech: Converts text responses back to speech using the pyttsx3 library.
*Web browsing: Opens websites in your default web browser based on your commands.
*Weather information: Fetches weather data using the OpenWeatherMap API and speaks the current temperature and description for a specified city.
*Time: Retrieves and speaks the current time.
*Music playback: Plays music from a specified directory on your computer.


Requirements:
*Python 3
*SpeechRecognition
*pyttsx3
*webbrowser
*requests (for weather API)
*os (for music playback)
*An API key from OpenWeatherMap (for weather information)


Instructions:
*Install the required libraries using pip install speech_recognition pyttsx3 webbrowser requests os.
*Replace YOUR_OPENWEATHERMAP_API_KEY in the script with your actual OpenWeatherMap API key.
*Replace YOUR_MUSIC_DIRECTORY_PATH in the script with the path to your music directory.
8Run the script using python assistant.py.


Usage:
Speak your commands to the virtual assistant and it will respond accordingly.
Here are some examples:
"Open YouTube"
"Open Google"
"What time is it?"
"What's the weather like in Bangalore?" (Replace Bangalore with your desired city)
"Play music"
"Exit"




import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import requests
import subprocess

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio input and recognize speech"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "None"
    return query.lower()

def open_website(url):
    """Open a website"""
    webbrowser.open(url)
    speak(f"Opening {url}")

def get_weather(city):
    """Fetch and speak the weather information"""
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    try:
        response = requests.get(complete_url)
        weather_data = response.json()

        if weather_data["cod"] != "404":
            main = weather_data["main"]
            temperature = main["temp"]
            weather_desc = weather_data["weather"][0]["description"]
            speak(f"The temperature in {city} is {temperature - 273.15:.2f} degrees Celsius with {weather_desc}.")
        else:
            speak("City not found.")
    except Exception as e:
        speak("There was an error fetching the weather data.")

def get_time():
    """Fetch and speak the current time"""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def play_music():
    """Play music from a specified directory"""
    music_dir = 'YOUR_MUSIC_DIRECTORY_PATH'
    songs = os.listdir(music_dir)
    if songs:
        song_path = os.path.join(music_dir, songs[0])
        if os.name == 'nt':  # For Windows
            os.startfile(song_path)
        else:  # For macOS and Linux
            subprocess.call(["open" if os.name == 'posix' else "xdg-open", song_path])
        speak("Playing music.")
    else:
        speak("No music files found in the directory.")

def perform_task(query):
    """Perform tasks based on the recognized query"""
    if 'open youtube' in query:
        open_website("https://www.youtube.com")
    elif 'open google' in query:
        open_website("https://www.google.com")
    elif 'time' in query:
        get_time()
    elif 'weather' in query:
        speak("Which city?")
        city = listen()
        if city != "None":
            get_weather(city)
    elif 'play music' in query:
        play_music()
    elif 'exit' in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command. Please try again.")

if __name__ == "__main__":
    speak("How can I assist you today?")
    while True:
        query = listen()
        if query and query != "None":
            perform_task(query)
