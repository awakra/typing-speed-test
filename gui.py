import tkinter as tk
from timer import Timer
from logic import TypingTestLogic

class TypingTestApp:
    def __init__(self):
        self.logic = TypingTestLogic()
        self.root = tk.Tk()
        self.root.title("Typing Speed Test")

        # Label to display the timer
        self.timer_label = tk.Label(self.root, text="Time left: 60", font=("Arial", 16))
        self.timer_label.pack(pady=10)

        # Label to display the word
        self.word_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.word_label.pack(pady=20)

        # User input
        self.entry = tk.Entry(self.root, font=("Arial", 18))
        self.entry.pack(pady=10)
        self.entry.bind("<Key>", self.on_first_keypress)
        self.entry.bind("<Return>", self.check_word)  # Pressing Enter calls check_word

        # Start/Next buttons
        self.next_button = tk.Button(self.root, text="Next Word", command=self.next_word)
        self.next_button.pack(pady=10)

        # Timer setup
        self.timer = Timer(
            root=self.root,
            duration=60,
            update_callback=self.update_timer_label,
            end_callback=self.end_test
        )

        self.next_word()

    def on_first_keypress(self, event):
        if not self.timer.is_running():
            self.timer.start()

    def next_word(self):
        self.current_word = self.logic.get_word()
        self.word_label.config(text=self.current_word)
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def check_word(self, event=None):
        typed = self.entry.get().strip()
        if typed == self.current_word:
            self.next_word()
        else:
            self.word_label.config(text=f"Error! It was: {self.current_word}")
            self.root.after(1000, self.next_word)

    def update_timer_label(self, time_left):
        self.timer_label.config(text=f"Time left: {time_left}")

    def end_test(self):
        self.entry.config(state='disabled')
        self.timer_label.config(text="Time's up!")

    def run(self):
        self.root.mainloop()