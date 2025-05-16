# Typing Speed Test

A desktop application to test and improve your typing speed!

This project provides a simple, interactive GUI for measuring your **words per minute (WPM)**, **characters per minute (CPM)**, and **accuracy**, with instant feedback and a retry option.

---

## Features

-  Random word prompts from a customizable word list
-  Countdown timer (default: 60 seconds) that starts on your first keystroke
-  Live scoring: tracks correct words, correct characters, WPM, CPM, and accuracy
-  Error feedback: shows the correct word if you make a mistake
-  Results summary at the end of each test
-  **Try Again** button to quickly restart the test
- Error handling with user-friendly popups

---

## Installation

### Clone the repository:

```bash
git clone https://github.com/awakra/typing-speed-test.git
cd typing-speed-test
```

### Install requirements:

This project uses only Python’s standard library (**Tkinter**).  
If you’re using Python 3, Tkinter is usually included by default.

---

## Usage

Run the application with:

```bash
python main.py
```

A window will appear with a word prompt and a text entry box.

- Start typing; the timer will begin on your first keystroke.
- Press `Enter` to submit each word.
- Your score and stats will be displayed when time is up.
- Click **Try Again** to restart the test.

---

## File Structure

```
main.py         – Entry point for the application
gui.py          – GUI logic and user interface
logic.py        – Typing test logic and word management
timer.py        – Countdown timer class
score.py        – Scoring and statistics logic
data.py         – Data handling (e.g., loading word lists)
words_alpha.txt – Word list used for prompts
.gitignore      – Standard python git ignore file
```

---

## Customization

### Change the timer duration:

Edit the `duration` parameter in `timer.py` or where the `Timer` is instantiated in `gui.py`.

### Use your own word list:

Replace `words_alpha.txt` with your preferred list of words (one word per line).

