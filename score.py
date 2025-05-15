import time

class Score:
    def __init__(self):
        self.correct_words = 0
        self.incorrect_words = 0
        self.total_words = 0
        self.correct_chars = 0
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()

    def add_correct(self, word):
        self.correct_words += 1
        self.total_words += 1
        self.correct_chars += len(word)

    def add_incorrect(self):
        self.incorrect_words += 1
        self.total_words += 1

    def get_elapsed_minutes(self):
        if self.start_time is None or self.end_time is None:
            return 1e-6  # Avoid division by zero
        elapsed = (self.end_time - self.start_time) / 60
        return max(elapsed, 1e-6)  # Avoid division by zero

    def get_wpm(self):
        return self.correct_words / self.get_elapsed_minutes()

    def get_cpm(self):
        return self.correct_chars / self.get_elapsed_minutes()

    def get_accuracy(self):
        if self.total_words == 0:
            return 0
        return (self.correct_words / self.total_words) * 100