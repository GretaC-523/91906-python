import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Function to display the current date and time
def create_welcome_screen(self):
    self.welcome_frame = tk.Frame(self.master)
    self.welcome_frame.pack(expand=True)

    welcome_label = tk.Label(
        self.welcome_frame,
        text="Welcome to the Hiragana & Katakana game.ひらがなとカタカナのゲームへようこそ。",
        font=("Arial", 18),
        fg="#4B0082",
        pady=10
    )
    welcome_label.pack()

    now = datetime.now()
    date_time_label = tk.Label(
    self.welcome_frame,
    text=now.strftime("The current date & time is(今の日付と時刻は): %A, %d %B %Y\n⏰%I:%M %p"),
    font=("Arial", 12),
    fg="#555555",
    pady=10
    )
    date_time_label.pack()