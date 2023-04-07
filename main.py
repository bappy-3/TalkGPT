// © Al Mustafiz Bappy
// created by Al Mustafiz Bappy at February 23, 2023 - 12∶12∶37
// Audio version for chatGPT

import openai
import time
import speech_recognition as sr
import pyttsx3

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Set up text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180) # Set the speaking rate to 180 words per minute

# Define a function to get text from speech
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    print("Recognizing...")
    try:
        # Use Google Web Speech API to recognize speech
        voice_input = r.recognize_google(audio)
        print(f"You said: {voice_input}")
        return voice_input
    except:
        print("Sorry, I could not understand what you said.")
        return None

# Define a function to convert text to speech
def give_voice_output(text):
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()

# Define a function to get OpenAI GPT-3 response
def get_gpt_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# Get user input and return OpenAI GPT-3 response
voice_input = get_voice_input()
if voice_input:
    prompt = f"You: {voice_input}\nTalkGPT:"
    response = get_gpt_response(prompt)
    print(response)
    give_voice_output(response)

