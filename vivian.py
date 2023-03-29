# ______________________________________________ #
# __      _________      _______          _   _  #
# \ \    / /_   _\ \    / /_   _|   /\   | \ | | #
#  \ \  / /  | |  \ \  / /  | |    /  \  |  \| | #
#   \ \/ /   | |   \ \/ /   | |   / /\ \ | . ` | #
#    \  /   _| |_   \  /   _| |_ / ____ \| |\  | #
#     \/   |_____|   \/   |_____/_/    \_\_| \_| #
# ______________________________________________ #

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
    engine.runAndWait() # synchronous speech blocking


if __name__ == "__main__":
    print("\nSystem Online\n"), speak("System Online")


def listenForCommand():
    """Listens for voice commands using the mic and speech_recognition library"""
    listener = sr.Recognizer()
    print("\nAwaiting command input\n"), speak("Awaiting command input")
    with sr.Microphone() as source:
        listener.pauseThreshold = 2 # pause after user finishes speaking, then processes
        inputSpeech = listener.listen(source)

    try:
        print("\nProcessing Speech...\n"), speak("Processing Speech...")
        command = listener.recognize_google(inputSpeech, language="en_gb")
        print(f"The input speech was: {command}")
        
        if "vivian" in command.lower():
            command = command.lower().replace("vivian", "").strip() # remove keyword from command 
            return command
        else:
            speak("I'm sorry, I didn't hear the keyword, Vivian")
            command = listenForCommand()
        
    except Exception as exception:
        speak("I could not understand that")
        print(exception)
        return "None"
    
# main loop to listen for voice commands and respond
while True:
    command = listenForCommand()
    if command:

        # greetings command
        if any(phrase in command.lower() for phrase in ["hello", "hi", "hey"]):
            speak("Hello there! Ashton")

        # goodbye command
        elif any(phrase in command.lower() for phrase in ["goodbye", "shut down", "terminate", "stop"]):
            speak("Shutting Down")
            exit()
            
        # name command
        elif any(phrase in command.lower() for phrase in ["what is your name", "who are you", "what are you called", "what are you"]):
            speak("My name is Vivian, I am an AI assisstant program")

        # VIVIAN meaning command
        elif any(phrase in command.lower() for phrase in ["what does vivian mean", "what does vivian stand for"]):
            speak("My name, Vivian, stands for, Virtually Interactive Voice Intelligent Artificial Network")

        # purpose command
        elif any(phrase in command.lower() for phrase in [ "what are you for", "what is your purpose", "why were you created"]):
            speak("I was created as an AI model for assissting you in any way I can")    

        # functions command
        elif any(phrase in command.lower() for phrase in ["What do you do", "what can you do", ""]):
            speak("I was created as an AI model for assissting you in any way I can")  

    # unrecognized command
    else:
        speak("I'm sorry, I didn't understand that command")

