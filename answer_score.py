import time
import random
from tkinter import messagebox
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Check and display the answer messages
def check_answer(self):
    kana, romaji = self.questions[self.current]
    answer = self.entry.get().strip().lower()

    if len(answer) < 2:
        messagebox.showwarning("Input Too Short", "Please enter at least 2 English letters.")
        return
    elif len(answer) > 3:
        messagebox.showwarning("Input Too Long", "Please enter no more than 3 English letters.")
        return

    if answer == romaji:
        self.correct += 1
        messagebox.showinfo("Correct! 正解です！")
    elif answer != romaji:
        messagebox.showinfo(text=f"Incorrect. The answer is '{self.correct_answer}' .", fg=self.colors['incorrect'])
    else:
        messagebox.showwarning("Invalid input. Please only enter romaji.")
        return

    self.current += 1
    self.next_question()

# Show the final results(scores) after the quiz ends
def show_results(self):
  total = len(self.questions)
  score_msg = f"You have answered {self.correct} out of {total} questions correctly.\n"
  score_msg.configure(fg="Courier New", bg="#F0F8FF")
  messagebox.showinfo("This is the end of the quiz. Good bye!", score_msg) 
  messagebox.configure(fg="Courier New", bg="#F0F8FF")
  self.master.quit()