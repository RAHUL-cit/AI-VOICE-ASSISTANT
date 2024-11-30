import pyttsx3
import webbrowser
import time
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Initialize the pyttsx3 engine for text-to-speech
engine = pyttsx3.init()

# Function to handle speech output
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError as e:
        print(f"Error: {e}")

# Function to handle command execution
def execute_command(command):
    command = command.lower()  # Convert to lowercase for easier comparison

    if "hello" in command:
        response = "Hello, how can I assist you today?"
    elif "goodbye" in command:
        response = "Goodbye! Have a nice day."
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube."
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        response = "Opening Google."
    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        response = "Opening WhatsApp."
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        response = "Opening Instagram."
    elif "open news" in command:
        webbrowser.open("https://www.indiatoday.in")
        response = "Opening India Today's News."
    elif "what is the time" in command:
        current_time = time.strftime("%H:%M:%S")
        response = f"The current time is {current_time}."
    elif "music" in command:
        webbrowser.open("https://www.spotify.com")
        response = "Opening Spotify."
    elif "mail" in command:
        webbrowser.open("https://www.gmail.com")
        response = "Opening Gmail."
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        response = "Opening Facebook."
    elif "open twitter" in command:
        webbrowser.open("https://www.twitter.com")
        response = "Opening Twitter."
    else:
        response = "I'm sorry, I didn't understand that command."
    
    speak(response)  # Speak out the response
    return response

# Route to serve the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to process commands
@app.route('/process-command/<command>', methods=['GET'])
def process_command(command):
    try:
        response = execute_command(command)
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error processing command: {e}")
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
