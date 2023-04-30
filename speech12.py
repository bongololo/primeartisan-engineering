import streamlit as st 
import pyttsx3
import speech_recognition as sr
import mysql.connector

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return "am not getting you."

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="timothy"
        )
        return conn
    except:
        print("Error connecting to database.")
        return None

def main():
    speak("welcome to voice based email please follow instructions .")
    speak("Please say your name.")
    name = listen()
    st.write(f"you said : {name}")
    speak("Please say your email address.")
    email = listen() 
    st.write(f"you said:  {email}")
    speak("please tell us your password.")
    password=listen()
    st.write (f"you said: {password}")
   
   

    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        sql = "INSERT INTO users (name, email,password) VALUES (%s, %s,%s)"
        val = (name, email,password )
        cursor.execute(sql, val)
        conn.commit()
        print(cursor.rowcount, "record inserted.")
        speak("you have succeffully registered.")
        conn.close()

if __name__ == "__main__":
    main()
