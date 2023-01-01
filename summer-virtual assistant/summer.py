# To enable the AI to listen to our voice speech 
import speech_recongnition as sr
# To speak out, or text to speech
import pyttsx3
# For advance control on browser
import pywhatkit
# to get date and time
import datetime
# To get wikipedia data
import wikipedia
# to get something funny
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_goggle(voice)
            command = command.lower()
            if 'summer' in command:
                command = command.replace('summer', '')
                print(command)
    except:
        pass
    return command

def run_summer():
    command = take_command()
    print(command)
    if 'play music' in command:
        song = command.replace('play', '')
        talk('playing ', + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('sorry, I do not eat')
    elif 'Are you single?' in command:
        talk('I am in a relationship with your Wi-Fi')
    else:
        talk('Please say the command again.')

while True:
    run_summer()
