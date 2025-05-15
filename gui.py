import tkinter as tk
from logic import TypingTestLogic

class TypingTestApp:
    def __init__(self):
        self.logic = TypingTestLogic()
        self.root = tk.Tk()
        self.root.title("Typing Speed Test")

        # Label to display the word
        self.word_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.word_label.pack(pady=20)

        # User input
        self.entry = tk.Entry(self.root, font=("Arial", 18))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)  # Pressionar Enter chama check_word

        # Start/Next buttons
        self.next_button = tk.Button(self.root, text="Next Word", command=self.next_word)
        self.next_button.pack(pady=10)

        self.next_word() 

    def next_word(self):
        self.current_word = self.logic.get_word()
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def check_word(self, event=None):
        typed = self.entry.get().strip()
        if typed == self.current_word:
            self.next_word()
        else:
            self.word_label.config(text=f"Error! It was: {self.current_word}")
            self.root.after(1000, self.next_word)  # Mostra o erro por 1 segundo

    def run(self):
        self.root.mainloop()