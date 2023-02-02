import speech_recognition, pyttsx3, pywhatkit, datetime, openai, secret_key

openai.api_key = secret_key.get_key()
listner = speech_recognition.Recognizer()
VIRTUAL_ASSISTANT_NAME = "computer"
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
            voice = listner.listen(source,None,5)
            command = listner.recognize_google(voice)
            print(command)
            command = command.lower()
            # if VIRTUAL_ASSISTANT_NAME in command:
            #     command = command.replace(VIRTUAL_ASSISTANT_NAME, "")
    except:
        command = ""
        pass
    
    return command
def generate_response(user_input):
    # Use the openai API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{user_input}",
        max_tokens=1024,
        temperature=0.5
    )
    # Return the generated response
    return response["choices"][0]["text"]


def run(): 
    while True:
        print("Listening...")
        speech = take_command()
        if VIRTUAL_ASSISTANT_NAME in speech:
            #winsound.PlaySound('listening.mp3',winsound.SND_FILENAME)
            if 'time' in speech:
                time_now = datetime.datetime.now().strftime('%I:%M %p')
                date = datetime.datetime.today().weekday()
                day = ""
                match date:
                    case 0:
                        day = "Monday"
                    case 1:
                        day = "Tuesday"
                    case 2:
                        day = "Wednesday"
                    case 3:
                        day = "Thursday"
                    case 4:
                        day = "Friday"
                    case 5:
                        day = "Saturday"
                    case 6:
                        day = "Sunday"
                        
                print(time_now)
                time_str = "The time is " + time_now + " of " + day
                say(time_str)
            elif 'play' in speech:
                song = speech.replace('hi','')
                song = song.replace('play','')
                song = song.replace(VIRTUAL_ASSISTANT_NAME,'')
                say("Playing"+ song)
                pywhatkit.playonyt(song)
            elif 'how are you' in speech:
                print("I am very well. Thanks for asking!! I hope you're doing well too. If I can help with anything just ask")
                say("I am very well. Thanks for asking!! I hope you're doing well too. If I can help with anything just ask")
            elif 'who are you' in speech:
                print("I am your virtual assistant. I am here to help you with anything you need.")
                say("I am your virtual assistant. I am here to help you with anything you need.")
            else:
                response = generate_response(speech)
                say(response)


run()