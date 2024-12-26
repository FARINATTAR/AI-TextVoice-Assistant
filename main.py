import os
import speech_recognition as sr
from googletrans import Translator
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    print("API key not found. Please set the GEMINI_API_KEY environment variable in the .env file.")
else:
    # Configure the Generative AI with the API key
    genai.configure(api_key=api_key)

# Initialize the translator
translator = Translator()

def get_voice_input():
    """Capture voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... (You can speak your question or type it instead)")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="auto")
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Error with the speech recognition service."

def translate_to_english(text):
    """Translate the text to English if it's not already in English."""
    translated = translator.translate(text, dest="en")
    print(f"Translated to English: {translated.text}")
    return translated.text

def get_gemini_response(query):
    """Fetch a response from Google Generative AI."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(query)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        print("\n--- Say something or type 'exit' to quit ---")
        
        # Check if user wants to exit
        choice = input("Would you like to type your question or speak it? (type/speak): ").strip().lower()
        
        if choice == 'exit':
            print("Goodbye!")
            break
        elif choice == 'speak':
            user_input = get_voice_input()  # Get voice input
        elif choice == 'type':
            user_input = input("Type your question: ").strip()  # Get typed input
        else:
            print("Invalid choice. Please type 'type' or 'speak'.")
            continue
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Translate input to English if needed
        english_input = translate_to_english(user_input)
        
        # Get response from Google Generative AI
        response = get_gemini_response(english_input)
        print(f"AI Response: {response}")

if __name__ == "__main__":
    main()
