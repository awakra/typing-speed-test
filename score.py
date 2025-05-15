import time

class Score:
    def __init__(self):
        """
        Initializes the Score class with attributes to track typing test statistics.

        Attributes:
            correct_words (int): The number of correctly typed words.
            incorrect_words (int): The number of incorrectly typed words.
            total_words (int): The total number of words typed.
            correct_chars (int): The number of correctly typed characters.
            start_time (float or None): The start time of the typing test.
            end_time (float or None): The end time of the typing test.
        """
        self.correct_words = 0
        self.incorrect_words = 0
        self.total_words = 0
        self.correct_chars = 0
        self.start_time = None
        self.end_time = None

    def start(self):
        """
        Starts the timer by recording the current time.

        This method initializes the `start_time` attribute with the current
        time in seconds since the epoch, using the `time.time()` function.
        """
        self.start_time = time.time()

    def end(self):
        """
        Marks the end time of the typing speed test.

        This method records the current time as the end time of the test
        using the `time.time()` function.
        """
        self.end_time = time.time()

    def add_correct(self, word):
        """
        Updates the score by incrementing the count of correct words, 
        total words, and the number of correct characters based on 
        the length of the provided word.

        Args:
            word (str): The word that was correctly typed.
        """
        self.correct_words += 1
        self.total_words += 1
        self.correct_chars += len(word)

    def add_incorrect(self):
        """
        Increments the count of incorrect words and the total word count.

        This method is used to track the number of words that were typed
        incorrectly during the typing speed test. It also updates the total
        word count to reflect the addition of an incorrect word.
        """
        self.incorrect_words += 1
        self.total_words += 1

    def get_elapsed_minutes(self):
        """
        Calculate the elapsed time in minutes between the start and end times.

        Returns:
            float: The elapsed time in minutes. If either `start_time` or `end_time` 
            is not set, or if the calculated elapsed time is less than a very small 
            threshold (1e-6), a default value of 1e-6 is returned to avoid division 
            by zero or negative elapsed time.
        """
        if self.start_time is None or self.end_time is None:
            return 1e-6  # Avoid division by zero
        elapsed = (self.end_time - self.start_time) / 60
        return max(elapsed, 1e-6)  # Avoid division by zero

    def get_wpm(self):
        """
        Calculate the words per minute (WPM) typing speed.

        Returns:
            float: The typing speed in words per minute, calculated as the number 
            of correctly typed words divided by the elapsed time in minutes.
        """
        return self.correct_words / self.get_elapsed_minutes()

    def get_cpm(self):
        """
        Calculate the characters per minute (CPM) based on the number of correct characters typed 
        and the elapsed time in minutes.

        Returns:
            float: The number of correct characters typed per minute.
        """
        return self.correct_chars / self.get_elapsed_minutes()

    def get_accuracy(self):
        """
        Calculate the typing accuracy as a percentage.

        Returns:
            float: The accuracy percentage, calculated as the ratio of correct words 
            to total words multiplied by 100. Returns 0 if no words were typed.
        """
        if self.total_words == 0:
            return 0
        return (self.correct_words / self.total_words) * 100