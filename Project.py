import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hello sir, what can i do for you?')
engine.runAndWait()






def talk(text):
    engine.say(text)
    engine.runAndWait()
    


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                print("Who is Siri, i dont know her, should i be worried?")
                engine.say("Who is Siri, i dont know her, should i be worried?")
                engine.runAndWait()
            elif 'alexa' in command:
                print("Who is Alexa, i dont know her, should i be worried?")
                engine.say("Who is Alexa, i dont know her, should i be worried?")
                engine.runAndWait()
            elif 'maya' in command:
                command = command.replace('maya', '')
                print(command)
                
    except:
        pass
    return command

def run_maya():
   
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    
while True:
    run_maya()