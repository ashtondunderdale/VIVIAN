import pyttsx3
import speech_recognition as sr

# engine initialization
engine = pyttsx3.init()

engine.setProperty('rate', 150) # rate of speech ( wpm )
engine.setProperty('volume', 1.0) # loudness, 0 = silent, 1 = max 

engine.setProperty('language', 'en-gb') # set English dialect
engine.setProperty('voice', engine.getProperty('voices')[0].id) # sets engine voice 


def speak(text):
    """Configures text-to-speech engine with speech properties"""
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    print("\nSystem Online\n"), speak("System Online")


def listenForCommand():
    """Listens for voice commands using the mic and speech_recognition library"""
    listener = sr.Recognizer()
    print("\nAwaiting command input\n"), speak("Awaiting command input")
    with sr.Microphone() as source:
        listener.pauseThreshold = 2
        inputSpeech = listener.listen(source)

    try:
        print("\nProcessing Speech...\n"), speak("Processing Speech...")
        command = listener.recognize_google(inputSpeech, language="en_gb")
        print(f"The input speech was: {command}")
    except Exception as exception:
        speak("I could not understand that")
        print(exception)
        return "None"
    
    return command

# main loop to listen for voice commands and respond
while True:
    command = listenForCommand()
    if command:
        if "hello" in command.lower():
            engine.say("Hello, Ashton")
            engine.runAndWait() # synchronous speech blocking

        elif "goodbye" in command.lower():
            engine.say("Shutting Down")
            engine.runAndWait()
            exit()
            break
