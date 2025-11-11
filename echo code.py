import os
import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import subprocess
import shlex
import random
import pyjokes


voices = engine.getProperty("voices")
engine.setProperty("rate", 175)  

if voices:
    engine.setProperty("voice", voices[0].id)  

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Network issue with recognition service.")
        return ""



def ask_ai(prompt):
    try:
        command = ["ollama", "run", "mistral", prompt]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        else:
            return "AI fallback failed or returned empty response."
    except FileNotFoundError:
        return "Ollama CLI not found. Make sure it's installed and in PATH."
    except Exception as e:
        return f"AI fallback failed: {e}"


memory_file = "assistant_memory.txt"

def remember(note):
    with open(memory_file, "a") as f:
        f.write(note + "\n")
    speak("Got it, I’ll remember that.")

def recall():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            notes = f.read().strip()
        return notes if notes else "I don’t remember anything yet."
    else:
        return "I don’t remember anything yet."


def process_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")

    elif "remember" in command:
        note = command.replace("remember", "").strip()
        if note:
            remember(note)
        else:
            speak("What should I remember?")

    elif "recall" in command or "what do you remember" in command:
        notes = recall()
        speak(notes)

    elif "calculate" in command:
        try:
            expression = command.replace("calculate", "").strip()
            expression = expression.replace("x", "*")
            result = eval(expression)
            speak(f"The result is {result}")
        except:
            speak("Sorry, I couldn’t calculate that.")

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif "coin" in command:
        result = random.choice(["Heads", "Tails"])
        speak(f"The coin landed on {result}.")

    elif "dice" in command:
        result = random.randint(1, 6)
        speak(f"You rolled a {result}.")

    else:
        ai_reply = ask_ai(command)
        speak(ai_reply)


if __name__ == "__main__":
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        cmd = listen()
        if cmd == "":
            continue
        if "exit" in cmd or "quit" in cmd or "stop" in cmd:
            speak("Goodbye!")
            break
        process_command(cmd)
