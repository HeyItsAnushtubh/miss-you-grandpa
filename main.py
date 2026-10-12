import speech_recognition as sr

def takeCommand():
    # Initializes the recognizer
    r = sr.Recognizer()
    
    # Removed the hardcoded '0' to use the default system microphone
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... please wait.")
        r.adjust_for_ambient_noise(source, duration=1) # Added this to calibrate the mic
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        # Using Google's free API. Requires an active internet connection.
        words = r.recognize_google(audio, language='mr-in')
        print(f"Speaker: {words}\n")
        return words

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio. Speak again.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

if __name__ == '__main__':
    takeCommand()