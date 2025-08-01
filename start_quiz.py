import time
import random
from tkinter import messagebox
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Function of the Kana quiz
def start_quiz(self, question_set):
 self.option_frame.destroy()
 
 self.questions = random.sample(question_set, 10)
 self.current = 0
 self.correct = 0

 self.quiz_label = tk.Label(self.master, text="", font=("Arial", 24))
 self.quiz_label.pack(pady=20)

 self.entry = tk.Entry(self.master, font=("Arial", 14))
 self.entry.pack()

 self.submit_btn = tk.Button(self.master, text="Submit", command=self.check_answer)
 self.submit_btn.pack(pady=10)

 self.next_question()

def start_hiragana(self):
 self.start_quiz(self.hiragana)

def start_katakana(self):
 self.start_quiz(self.katakana)

def start_both(self):
 self.start_quiz(self.hiragana + self.katakana)

def next_question(self):
 if self.current < len(self.questions):
     kana, _ = self.questions[self.current]
     self.quiz_label.config(text=kana)
     self.entry.delete(0, tk.END)
 else:
     self.show_results()
