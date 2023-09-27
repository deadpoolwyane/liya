import speech_recognition as sr
import pyttsx3
from datetime import date
#import cv2
from time import sleep

pir = 2
touch =3



filename ="op_list.txt"


# Create a recognizer object
recognizer = sr.Recognizer()

engine = pyttsx3.init()

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

# variables
    
name = []

ages = []

address = []

gender = []

def speak_text(a2):
    engine.say(a2)
    engine.runAndWait()
def recognize_speech():
    #if pir==1:

    with sr.Microphone() as source:

        print("Listening...")

        audio = recognizer.listen(source)


    try:
        global name
        global ages
        global op_number
        global address
        #global num,nam
        text = recognizer.recognize_google(audio)
        lower = text.lower()
        if "name" in lower:
            name.append(lower)
        if "male" in lower:
            gender.append("Male")
        if "female" in lower:
            gender.append("Female")

        if "age" in lower:
            ages.append(lower)
        if "address" in lower:
            address.append(lower)
        if "list" in lower:
            print("hi")
            for num,nam in enumerate(name):
                print("op number :",num,"\n " ,nam)
                speak_text("the op number is ")
                speak_text(num)


                speak_text(nam)

                speak_text("the date is")
                speak_text(date.today())
                print(date.today())

                speak_text(address)
                for i in ages:

                    speak_text(i)
                    print(i)
                    break

                for o in gender:
                    speak_text(o)
                    print(o)
                    break

        #print("patient_name :", name)
        #print("patient_age :", age)
        #print(f"%s is the address",address)

        print("text :", text)

        #print(num, nam)
       # return text


    except sr.UnknownValueError:
        return "Sorry, I couldn't understand your speech."
    except sr.RequestError as e:
        return f"Speech recognition request failed: {e}"

while True:

    recognize_speech()
            