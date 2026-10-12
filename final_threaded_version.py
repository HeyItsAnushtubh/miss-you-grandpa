import tkinter as tk
import threading
import speech_recognition as sr

def listen_and_update(label, button):
    button.config(state="disabled") # Prevent spamclicking
    r = sr.Recognizer()
    
    label.config(text="Adjusting noise... wait.")
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        label.config(text="Listening... Speak now.", fg="blue")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        label.config(text="Recognizing...", fg="orange")    
        words = r.recognize_google(audio, language='mr-in')
        label.config(text=words, fg="green")
    except sr.UnknownValueError:
        label.config(text="Didn't catch that. Try again.", fg="red")
    except sr.RequestError:
        label.config(text="API Error. Check internet.", fg="red")
    finally:
        button.config(state="normal") # Turn button back on

def trigger_thread(label, button):
    # Fire the listening function in a separate thread so Tkinter doesn't lock up
    threading.Thread(target=listen_and_update, args=(label, button), daemon=True).start()

def build_gui():
    root = tk.Tk()
    root.geometry("600x400")
    root.title("Voice App")

    # Big text label
    output_label = tk.Label(root, text="Ready.", font=("Helvetica", 28, "bold"), wraplength=550, justify="center")
    output_label.pack(expand=True, fill="both", padx=20, pady=20)

    # Trigger button
    listen_btn = tk.Button(root, text="Start Listening", font=("Helvetica", 16))
    # We map the command after creating the button so we can pass the button itself as an argument
    listen_btn.config(command=lambda: trigger_thread(output_label, listen_btn))
    listen_btn.pack(side="bottom", pady=40)

    root.mainloop()

if __name__ == '__main__':
    build_gui()