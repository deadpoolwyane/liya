import speech_recognition as sr
import pyttsx3

# Create a recognizer object
recognizer = sr.Recognizer()

engine = pyttsx3.init()

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

# variables

name = []

ages = []

op_number = 1

def speak_text(a2):
    engine.say(a2)
    engine.runAndWait()
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        global op_number
        global patients

        text = recognizer.recognize_google(audio)
        lower = text.lower()

        # Check if the user provided their name
        if "name" in lower:
            # Create a new patient record
            patient = {"name": "", "age": "", "gender": ""}
            patients.append(patient)
            op_number += 1  # Increment the operation number for each new entry

            speak_text(f"Please provide the name for Operation Ticket {op_number}")

        # Check if the user provided their age
        elif "age" in lower:
            if op_number > 0:
                # Assume that the last created patient record is the current one
                current_patient = patients[op_number - 1]
                current_patient["age"] = text
                speak_text(f"Please provide the gender for Operation Ticket {op_number}")
            else:
                speak_text("Please provide your name first.")

        # Check if the user provided their gender
        elif "male" in lower or "female" in lower:
            if op_number > 0:
                # Assume that the last created patient record is the current one
                current_patient = patients[op_number - 1]
                current_patient["gender"] = text
                speak_text(f"Thank you. Operation Ticket {op_number} details recorded.")
            else:
                speak_text("Please provide your name and age first.")

        # Check for "list" to list the details
        elif "list" in lower:
            for num, patient in enumerate(patients, start=1):
                print("Operation Ticket Number:", num)
                speak_text("Operation Ticket Number:")
                speak_text(num)
                speak_text("Name:")
                speak_text(patient["name"])
                speak_text("Age:")
                speak_text(patient["age"])
                speak_text("Gender:")
                speak_text(patient["gender"])

        print("text:", text)

    except sr.UnknownValueError:
        return "Sorry, I couldn't understand your speech."
    except sr.RequestError as e:
        return f"Speech recognition request failed: {e}"

# Initialize variables
op_number = 0  # Operation ticket number
patients = []  # List to store patient records

while True:
    recognize_speech()