import random

class VirtualAssistant:
    
    def __init__(self):
        self.greetings = ["Hello! How can I help you?", "Hi there! What can I do for you today?", "Greetings! What do you need assistance with?"]
        self.goodbyes = ["Goodbye!", "See you later!", "Have a great day!"]
        self.affirmations = ["Okay, I'll do that.", "Sure thing!", "No problem!", "I'm on it!"]
        self.negations = ["I'm sorry, I can't do that.", "I'm afraid I can't help with that.", "That's outside my capabilities."]
        self.unclear = ["I'm sorry, I didn't understand that.", "I'm not sure what you mean.", "I'm not sure I understand."]
    
    def greet(self):
        return random.choice(self.greetings)
    
    def goodbye(self):
        return random.choice(self.goodbyes)

    def affirm(self):
        return random.choice(self.affirmations)