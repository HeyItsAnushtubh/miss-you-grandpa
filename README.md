# miss-you-grandpa
A speech-to-text app I made for my grandfather to help him in his battle with cancer.

A lightweight, accessible Speech-to-Text application featuring a high-vis GUI. Originally built to help my grandfather easily dictate and read text on screen. 

The application listens to microphone input, processes it through Google's Speech Recognition API (configured for Marathi), and displays the transcribed text in a large, easy-to-read font. The GUI is multi-threaded to prevent application freezing during audio capture.

## Features
* **High-Visibility UI:** Large fonts and contrasting colors designed for visual accessibility.
* **Non-Blocking Execution:** Audio processing runs on a background daemon thread, keeping the Tkinter window responsive.
* **Native Language Support:** Hardcoded to recognize Marathi (`mr-in`) by default.
* **Visual Feedback:** Dynamic UI states indicate when the app is adjusting to noise, listening, processing, or encountering an error.

## Prerequisites
* Python 3.x
* An active internet connection (required for the Google Web Speech API)
* A working microphone

## Installation

1. **Clone or download** this repository.
2. **Install the required dependencies.** 
   *Note: Ensure you are installing these to the exact Python environment running the script.*
   ```bash
   pip install SpeechRecognition pyaudio
(If you encounter a ModuleNotFoundError later, run python -m pip install SpeechRecognition pyaudio using the absolute path to your specific Python executable).

Linux/Mac Users (Optional): If you encounter missing audio headers during pyaudio installation, you may need to install portaudio first:

Mac: brew install portaudio

Debian/Ubuntu: sudo apt-get install portaudio19-dev

## Usage
Run the application directly from your terminal or IDE:

python voice_app.py
Click "Start Listening", wait for the text to turn blue ("Listening... Speak now."), and speak into your microphone.
