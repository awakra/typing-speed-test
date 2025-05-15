from random import choice
from tkinter import messagebox
from data import get_word_list

class TypingTestLogic:
    """
    A class to handle the logic for a typing speed test application.
    Methods:
    --------
    __init__():
        Initializes the TypingTestLogic instance by loading a list of words.
        If the word list cannot be loaded or is empty, a default word list is used.
    get_word():
        Returns a random word from the loaded word list.
    """
    def __init__(self):
        try:
            self.words = get_word_list()
            if not self.words:
                raise ValueError("Wordlist is empty.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load wordlist: {e}")
            self.words = ["default"]

    
    def get_word(self):
        return choice(self.words)
    
