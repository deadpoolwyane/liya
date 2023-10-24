import speech_recognition as sr
import tkinter as tk
from tkinter import PhotoImage
import serial 
import pyttsx3 
import time as t
import csv 
import pyautogui as px
global count
count=0
global final_entry
global name_entry
global age_entry
global gender_entry
name_entry=None
age_entry=None
gender_entry=None
final_entry=None
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
    def collect_data():
        print("Serial OK")
        line=None
        try:
            line = communi.readline().decode("utf-8")
            px.alert(line)
            final_entry.delete(1.0, tk.END) 
            final_entry.insert(tk.END,line)
            communi.reset_intput_buffer()
        except KeyboardInterrupt:
            print("closing serial communication")
            communi.close()
    def recognize_speech(output_text,speakw):
        speak_text("what is your"+str(speakw))
        with sr.Microphone() as source:
            output_text.delete(1.0, tk.END)  # Clear the Text widget
            speak_text("listening")
            audio = recognizer.record(source,duration=4)
            speak_text("Finished Recording")
            output_text.delete(1.0, tk.END)  # Clear the "Listening..." message
        try:
            recognized_text = recognizer.recognize_google(audio)
            if recognized_text in 'mail':
                recognized_text="male"
                output_text.insert(tk.END, recognized_text)
            else:
                output_text.insert(tk.END, recognized_text) 
        except sr.UnknownValueError:
            speak_text("Google Web Speech Recognition could not understand audio.")
            output_text.insert(tk.END, "Google Web Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            output_text.insert(tk.END, f"Could not request results from Google Web Speech Recognition service; {e}")
  
    def submit_form():
        name = name_entry.get("1.0", "end-1c")  # Get the text from the Text widget
        age = age_entry.get("1.0", "end-1c")
        gender = gender_entry.get("1.0", "end-1c")
        fina=final_entry.get("1.0","end-1c")
        global count
        try:
            with open('data.csv', 'r', newline='') as input_file:
                reader = csv.reader(input_file)
                for row in reader:
                    last_row = row[0]
                    print(last_row)
                count=int(last_row)
        except FileNotFoundError:
            count=0
        count=count+1
        with open("data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([count,name,age,gender,fina])
        
        with open("file.txt",'w') as f:
            f.write("\n\n\n\n\n\n\n\n\nOP NO:"+str(count)+"\n"+"Name :"+str(name)+"\n"+"Age :"+str(age)+"\n"+"Gender :"+str(gender)+"\n"+"Recorded Data"+str(fina))
        # You can perform actions with the form data here
        print("Name:", name)
        print("Age:", age)
        print("Gender:", gender)
        print("The values taken by liya:",fina)
        name_entry.delete(1.0, tk.END)
        age_entry.delete(1.0, tk.END)
        gender_entry.delete(1.0, tk.END)
        final_entry.delete(1.0, tk.END)
        #root.destroy()
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
    name_label.pack(padx=10, pady=10)
    name_entry = tk.Text(root, height=1, width=40,font=("Arial", 15))
    name_entry.pack(padx=10, pady=10)

    recognize_name_button = tk.Button(root, text="Recognize Name", command=lambda: recognize_speech(name_entry,"name"),font=("Arial", 20))
    recognize_name_button.pack()

    age_label = tk.Label(root, text="Age:", font=("Arial", 20))
    age_label.pack(padx=10, pady=10)

    age_entry = tk.Text(root, height=1, width=40,font=("Arial", 15))
    age_entry.pack(padx=10, pady=10)

    recognize_age_button = tk.Button(root, text="Recognize Age", command=lambda: recognize_speech(age_entry,"age"),font=("Arial", 20))
    recognize_age_button.pack()

    gender_label = tk.Label(root, text="Gender:", font=("Arial", 20))
    gender_label.pack(padx=10, pady=10)

    gender_entry = tk.Text(root, height=1, width=40,font=("Arial",15))
    gender_entry.pack(padx=10, pady=10)

    recognize_gender_button = tk.Button(root, text="Recognize Gender", command=lambda: recognize_speech(gender_entry,"gender"),font=("Arial", 20))
    recognize_gender_button.pack()

    final_label = tk.Label(root, text="Final result are", font=("Arial", 20))
    final_label.pack(padx=10, pady=10)

    final_entry = tk.Text(root, height=1, width=40,font=("Arial", 15))
    final_entry.pack(padx=10, pady=10)

    collect_data_button = tk.Button(root, text="Generate Result", command=lambda: collect_data() ,font=("Arial", 20))
    collect_data_button.pack()

    submit_button = tk.Button(root, text="Submit", command=submit_form, font=("Arial", 20))
    submit_button.pack(padx=20, pady=20)

    exit_button =tk.Button(root, text="exit", command=root.destroy, font=("Arial", 25))
    exit_button.pack(padx=30, pady=30)

    # Start the main event loop
    root.mainloop()

gui()
