import tkinter as tk
import speech_recognition as sr

# Create the main application window
root = tk.Tk()
root.title("Speech Recognition with Tkinter")

# Create a Text widget to display recognized speech
output_text = tk.Text(root, height=10, width=40)
output_text.pack()

# Function to capture and display recognized speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        output_text.delete(1.0, tk.END)  # Clear the Text widget
        output_text.insert(tk.END, "Listening...")
        audio = r.listen(source)
        output_text.delete(1.0, tk.END)  # Clear the "Listening..." message
        try:
            recognized_text = r.recognize_google(audio)
            output_text.insert(tk.END, recognized_text)
        except sr.UnknownValueError:
            output_text.insert(tk.END, "Google Web Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            output_text.insert(tk.END, f"Could not request results from Google Web Speech Recognition service; {e}")

# Create a button to start speech recognition
recognize_button = tk.Button(root, text="Recognize Speech", command=recognize_speech)
recognize_button.pack()

# Start the main event loop
root.mainloop()
