import speech_recognition, pyttsx3, winsound, pywhatkit, datetime, os, time


listner = speech_recognition.Recognizer()
VIRTUAL_ASSISTANT_NAME = "baby"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice = engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)
def say(text):
    engine.say(text)
    engine.runAndWait()
say("Hi. I'm your" + VIRTUAL_ASSISTANT_NAME + ". How can I help you?")
def take_command():
    try:
        
        with speech_recognition.Microphone() as source:
            winsound.PlaySound('listening.mp3',winsound.SND_FILENAME)
            print("Listening...")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if VIRTUAL_ASSISTANT_NAME in command:
                command = command.replace(VIRTUAL_ASSISTANT_NAME, "")
                print(command)
    except:
        command = ""
        pass
    
    return command

def run():
    while True:
        speech = take_command()
        if 'time' in speech:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            print(time_now)
            say("Time rightnow is "+ time_now)
        elif 'play' in speech:
            song = speech.replace('play','')
            say("Playing"+ song)
            pywhatkit.playonyt(song)
            break
        elif 'how are you' in speech:
            say("I am very well. Thanks for asking!! I hope you're doing well too. If I can help with anything just ask")
        else:
            say("Sorry! Can you repeat that??")


run()