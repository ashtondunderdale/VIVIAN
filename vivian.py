import pyttsx3


# engine initialisation
engine = pyttsx3.init()

# engine properties
engine.setProperty('rate', 150) # rate of speech ( wpm )
engine.setProperty('volume', 1.0) # loudness, 0 = silent, 1 = max 

engine.setProperty('language', 'en-gb') # set English dialect
engine.setProperty('voice', engine.getProperty('voices')[0].id) # sets engine voice 

text = "Hello, my name is VIVIAN, how can I help?" # sample text

engine.say(text)
engine.runAndWait() # synchronous speech blocking

