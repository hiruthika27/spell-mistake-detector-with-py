import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

def detect_pronunciation_mistake(reference_text):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        messagebox.showinfo("Start Speaking", "Please start speaking now.")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        recognized_text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {recognized_text}")

        if recognized_text.lower() == reference_text.lower():
            result = "Great job! Your pronunciation was correct."
        else:
            result = f"Pronunciation Mistake Detected.\nExpected: {reference_text}\nHeard: {recognized_text}"

        messagebox.showinfo("Result", result)
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Could not request results from Google Speech Recognition service; {e}")

def on_submit():
    reference_text = entry.get()
    if reference_text:
        detect_pronunciation_mistake(reference_text)
    else:
        messagebox.showwarning("Input Error", "Please enter the reference text.")

# Setting up the GUI
root = tk.Tk()
root.title("Pronunciation Mistake Detector")

label = tk.Label(root, text="Enter the text:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

root.mainloop()
