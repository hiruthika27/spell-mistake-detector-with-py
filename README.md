# spell-mistake-detector-with-py
python project for understanding the working of py and its libraries

This project demonstrates the use of Python and several of its powerful libraries to create a Pronunciation Mistake Detector. The application features a graphical user interface (GUI) built with tkinter, integrates speech recognition capabilities with the speech_recognition library, and uses the pydub library for audio processing and playback.

Learning Objectives:
Python GUI Development: Learn to create a simple GUI using the tkinter library.
Speech Recognition: Understand how to use the speech_recognition library to capture and process audio input.
Audio Processing: Gain insight into audio processing using the pydub library, although in this code, pydub is imported but not directly utilized.
Features:
User Interface: Provides an easy-to-use interface for entering text and receiving feedback.
Real-Time Speech Recognition: Captures and recognizes spoken words in real-time.
Pronunciation Feedback: Compares recognized speech with the reference text and provides feedback on pronunciation accuracy.
How It Works:
The user enters a reference text into the provided text entry field.
Upon clicking the "Submit" button, the application prompts the user to start speaking.
The application listens to the user's speech through the microphone and uses Google's Speech Recognition API to convert it to text.
The recognized text is compared with the reference text, and feedback is displayed in a message box indicating whether the pronunciation was correct or if there were any mistakes.
