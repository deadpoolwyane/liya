import speech_recognition as sr
import tkinter as tk
from tkinter import PhotoImage
import serial 
import pyttsx3 
import time
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice','english')
line=None
communi = serial.Serial("/dev/ttyUSB0", 9600, timeout = 1.0)
t.sleep(3)
communi.reset_input_buffer()
# Function to handle form submission
def gui():
    def speak_text(text):
        engine.say(text)
        engine.runAndWait()
    def recognize_speech(output_text):
        with sr.Microphone() as source:
            output_text.delete(1.0, tk.END)  # Clear the Text widget
            speak_text("listening")
            audio = r.record(source,duration=4)
            speak_text("Finished Recording")
            output_text.delete(1.0, tk.END)  # Clear the "Listening..." message
        try:
            recognized_text = r.recognize_google(audio)
            if x in 'mail':
                recognized_text="male"
                output_text.insert(tk.END, recognized_text)
            else:
                output_text.insert(tk.END, recognized_text) 
        except sr.UnknownValueError:
            output_text.insert(tk.END, "Google Web Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            output_text.insert(tk.END, f"Could not request results from Google Web Speech Recognition service; {e}")

    def submit_form():
        line=None
        name = name_entry.get("1.0", "end-1c")  # Get the text from the Text widget
        age = age_entry.get("1.0", "end-1c")
        gender = gender_entry.get("1.0", "end-1c")
        try:
            while True:
                a=None
                t.sleep(5)
                if communi.in_waiting>0:
                    line = communi.readline().decode("utf-8")
                    print(line)
                    px.alert(line)
                    a=px.confirm('Enter option',buttons=['correct','wrong'])
                if a=='correct':
                    break
        except KeyboardInterrupt:
                print("closing serial communication")
                communi.close()

        root.destroy()
        # You can perform actions with the form data here
        print("Name:", name)
        print("Age:", age)
        print("Gender:", gender)


    # Create the main application window
    root = tk.Tk()
    root.title("Sample Form")

    # Maximize the window (works on Linux)
    root.attributes('-zoomed', True)

    # Load and display a custom background image
    background_image = PhotoImage(file="background.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Create and display form elements
    name_label = tk.Label(root, text="Name:", font=("Arial", 20))
    name_label.pack(padx=20, pady=20)
    name_entry = tk.Text(root, height=5, width=40)
    name_entry.pack(padx=20, pady=20)

    recognize_name_button = tk.Button(root, text="Recognize Name", command=lambda: recognize_speech(name_entry),font=("Arial", 20))
    recognize_name_button.pack()

    age_label = tk.Label(root, text="Age:", font=("Arial", 20))
    age_label.pack(padx=20, pady=20)

    age_entry = tk.Text(root, height=5, width=40)
    age_entry.pack(padx=20, pady=20)

    recognize_age_button = tk.Button(root, text="Recognize Age", command=lambda: recognize_speech(age_entry),font=("Arial", 20))
    recognize_age_button.pack()

    gender_label = tk.Label(root, text="Gender:", font=("Arial", 20))
    gender_label.pack(padx=20, pady=20)

    gender_entry = tk.Text(root, height=5, width=40)
    gender_entry.pack(padx=20, pady=20)

    recognize_gender_button = tk.Button(root, text="Recognize Gender", command=lambda: recognize_speech(gender_entry),font=("Arial", 20))
    recognize_gender_button.pack()

    final_label = tk.Label(root, text="Final result are", font=("Arial", 20))
    final_label.pack(padx=20, pady=20)

    final_entry = tk.Text(root, height=5, width=40)
    final_entry.pack(padx=20, pady=20)

    submit_button = tk.Button(root, text="Submit", command=submit_form, font=("Arial", 20))
    submit_button.pack(padx=20, pady=20)

    # Start the main event loop
    root.mainloop()

gui()
