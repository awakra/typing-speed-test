import tkinter as tk

class Timer:
    """
    Timer class provides a countdown timer functionality with callbacks for updates and completion.
    Attributes:
        root (tk.Tk): The root Tkinter window or widget to schedule the timer.
        duration (int): The total duration of the timer in seconds.
        time_left (int): The remaining time in seconds.
        update_callback (callable): A function to call every second with the remaining time as an argument.
        end_callback (callable): A function to call when the timer reaches zero.
        timer_job (int or None): The ID of the scheduled job in Tkinter, or None if no job is scheduled.
        running (bool): Indicates whether the timer is currently running.
    Methods:
        start():
            Starts the timer countdown if it is not already running.
        _tick():
            Internal method to handle the countdown logic and invoke callbacks.
        stop():
            Stops the timer and cancels any scheduled jobs.
        reset():
            Stops the timer and resets the remaining time to the initial duration.
        is_running() -> bool:
            Returns whether the timer is currently running.
    """
    def __init__(self, root, duration, update_callback, end_callback):
        self.root = root
        self.duration = duration
        self.time_left = duration
        self.update_callback = update_callback  # Called every tick
        self.end_callback = end_callback        # Called when timer ends
        self.timer_job = None
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.time_left = self.duration
            self._tick()

    def _tick(self):
        if self.time_left > 0:
            self.time_left -= 1
            if self.update_callback:
                self.update_callback(self.time_left)
            self.timer_job = self.root.after(1000, self._tick)
        else:
            self.running = False
            if self.end_callback:
                self.end_callback()

    def stop(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        self.running = False

    def reset(self):
        self.stop()
        self.time_left = self.duration

    def is_running(self):
        return self.running