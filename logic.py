from random import choice
from data import get_word_list

class TypingTestLogic:
    def __init__(self):
        try:
            self.words = get_word_list()
            if not self.words:
                raise ValueError("Wordlist is empty.")
        except Exception as e:
            print(f"Failed to load wordlist: {e}")
            self.words = ["default"] 

    
    def get_word(self):
        return choice(self.words)
    
