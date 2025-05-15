import tkinter as tk
from timer import Timer
from score import Score
from logic import TypingTestLogic

class TypingTestApp:
    def __init__(self):
        """
        Initializes the Typing Speed Test GUI application.
        This constructor sets up the main components of the GUI, including the timer,
        word display, user input field, and buttons. It also initializes the logic
        for the typing test and the scoreboard.
        Attributes:
            logic (TypingTestLogic): The logic handler for the typing test.
            root (tk.Tk): The main Tkinter window for the application.
            test_active (bool): A flag to indicate if the test is active.
            timer_label (tk.Label): A label to display the remaining time.
            word_label (tk.Label): A label to display the current word to type.
            entry (tk.Entry): An entry widget for user input.
            next_button (tk.Button): A button to load the next word.
            timer (Timer): A Timer instance to manage the countdown.
            score (Score): A Score instance to track the user's score.
        """
        self.logic = TypingTestLogic()
        self.root = tk.Tk()
        self.root.title("Typing Speed Test")
        self.test_active = True

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
        # Start the scoreboard instance
        self.score = Score()

        self.next_word()

    def on_first_keypress(self, event):
        """
        Handles the event triggered by the first keypress during the typing test.

        This method starts the score tracking and timer if the typing test is active
        and the timer is not already running.

        Args:
            event: The event object associated with the keypress.
        """
        if self.test_active and not self.timer.is_running():
            self.score.start()
            self.timer.start()

    def next_word(self):
        """
        Updates the GUI with the next word for the typing test.

        This method retrieves the next word from the logic component, updates the word
        label to display the new word, clears the text entry field, enables it for input,
        and sets focus to the entry field for the user to type.

        Returns:
            None
        """
        self.current_word = self.logic.get_word()
        self.word_label.config(text=self.current_word)
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def check_word(self, event=None):
        """
        Handles the event of checking the typed word against the current word.

        This method is triggered when the user submits a word (e.g., by pressing Enter).
        It compares the word entered in the input field with the current word displayed.
        If the words match, the score is updated for a correct word, and the next word is displayed.
        If the words do not match, the score is updated for an incorrect word, an error message
        is displayed, and the next word is shown after a short delay.

        Args:
            event (tkinter.Event, optional): The event object triggered by the key press. 
                                             Defaults to None.
        """
        typed = self.entry.get().strip()
        if typed == self.current_word:
            self.score.add_correct(self.current_word)
            self.next_word()
        else:
            self.score.add_incorrect()
            self.word_label.config(text=f"Error! It was: {self.current_word}")
            self.root.after(1000, self.next_word)

    def update_timer_label(self, time_left):
        """
        Updates the timer label with the remaining time.

        Args:
            time_left (int): The amount of time left in seconds to display on the timer label.
        """
        self.timer_label.config(text=f"Time left: {time_left}")

    def end_test(self):
        """
        Ends the typing speed test and updates the GUI accordingly.

        This method performs the following actions:
        - Sets the test_active flag to False, indicating the test has ended.
        - Finalizes the score by calling the `end` method of the score object.
        - Disables the text entry widget to prevent further input.
        - Disables the "Next" button to prevent further interaction.
        - Updates the timer label to indicate that the time is up.
        - Displays the final results of the test.

        This method is typically called when the test timer runs out or the test is manually ended.
        """
        self.test_active = False
        self.score.end()
        self.entry.config(state='disabled')
        self.next_button.config(state='disabled')  # Disable the button
        self.timer_label.config(text="Time's up!")
        self.display_results()
            
    def display_results(self):
        """
        Displays the results of the typing speed test on the GUI.
        This method calculates and formats the typing speed test results, including
        Words Per Minute (WPM), Characters Per Minute (CPM), accuracy percentage,
        the number of correct words, and the number of correct characters. It then
        displays these results in a label widget on the GUI. Additionally, it adds
        a "Try Again" button to allow the user to restart the test.
        Attributes:
            wpm (float): Words per minute calculated from the test.
            cpm (float): Characters per minute calculated from the test.
            accuracy (float): Accuracy percentage of the typing test.
            correct_chars (int): Total number of correctly typed characters.
            correct_words (int): Total number of correctly typed words.
        GUI Elements:
            result_label (tk.Label): A label widget displaying the formatted results.
            try_again_button (tk.Button): A button widget to restart the typing test.
        """
        wpm = self.score.get_wpm()
        cpm = self.score.get_cpm()
        accuracy = self.score.get_accuracy()
        correct_chars = self.score.correct_chars
        correct_words = self.score.correct_words

        result_text = (
            f"WPM: {wpm:.2f}\n"
            f"CPM: {cpm:.2f}\n"
            f"Accuracy: {accuracy:.2f}%\n"
            f"Correct Words: {correct_words}\n"
            f"Correct Characters: {correct_chars}"
        )

        self.result_label = tk.Label(self.root, text=result_text, font=("Arial", 16))
        self.result_label.pack(pady=20)

        self.try_again_button = tk.Button(self.root, text="Try Again", command=self.try_again)
        self.try_again_button.pack(pady=10)
    
    def try_again(self):
        """
        Resets the typing speed test to its initial state, allowing the user to try again.

        This method performs the following actions:
        - Destroys the result label and the "Try Again" button from the GUI.
        - Resets the score by creating a new Score instance.
        - Resets the timer and updates the timer label to show the initial time (60 seconds).
        - Enables the text entry field and the "Next" button for user interaction.
        - Prepares the next word for the typing test.
        - Clears the text entry field and sets focus on it.
        - Marks the test as active for further interaction.
        """
        self.result_label.destroy()
        self.try_again_button.destroy()
        self.score = Score()
        self.timer.reset()
        self.timer_label.config(text="Time left: 60")
        self.entry.config(state='normal')
        self.next_button.config(state='normal')  # Enable the button
        self.next_word()
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.test_active = True

    def run(self):
        """
        Starts the main event loop of the GUI application.

        This method initializes and runs the Tkinter main loop, 
        which listens for events and updates the GUI accordingly.
        """
        self.root.mainloop()