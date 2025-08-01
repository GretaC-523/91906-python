import time
import random
from tkinter import messagebox
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

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
        messagebox.showinfo("Your answer is correct!", "ビンゴ！")
    else:
        messagebox.showinfo("Your answer is incorrect.", f"It should be '{romaji}'.")

    self.current += 1
    self.next_question()

def show_results(self):
 total = len(self.questions)
 score_msg = f"You have answered {self.correct} out of {total} questions correctly.\n"
 messagebox.showinfo("This is the end of the quiz", score_msg)
 self.master.quit()