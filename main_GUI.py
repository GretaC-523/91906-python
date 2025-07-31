# author: Greta
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from list_display import kana_list
from main import Kana_quiz

class KanaQuizGUI:
    def __init__(self, master):
        self.master = master
        master.title("Kana Quiz 🌸")

        self.hiragana, self.katakana = kana_list()
        self.questions = []
        self.current = 0
        self.correct = 0
        self.incorrect = 0

        self.label = tk.Label(master, text="Choose quiz type:")
        self.label.pack()

        self.hira_btn = tk.Button(master, text="Hiragana", command=self.start_hiragana)
        self.hira_btn.pack()

        self.kata_btn = tk.Button(master, text="Katakana", command=self.start_katakana)
        self.kata_btn.pack()

        self.both_btn = tk.Button(master, text="Both", command=self.start_both)
        self.both_btn.pack()

        self.quiz_label = tk.Label(master, text="", font=("Arial", 24))
        self.entry = tk.Entry(master)
        self.submit_btn = tk.Button(master, text="Submit", command=self.check_answer)

    def start_hiragana(self):
        self.questions = random.sample(self.hiragana, 10)
        self.start_quiz()

    def start_katakana(self):
        self.questions = random.sample(self.katakana, 10)
        self.start_quiz()

    def start_both(self):
        combined = self.hiragana + self.katakana
        self.questions = random.sample(combined, 10)
        self.start_quiz()

    def start_quiz(self):
        self.label.pack_forget()
        self.hira_btn.pack_forget()
        self.kata_btn.pack_forget()
        self.both_btn.pack_forget()

        self.quiz_label.pack()
        self.entry.pack()
        self.submit_btn.pack()
        self.next_question()

    def next_question(self):
        if self.current < len(self.questions):
            kana, _ = self.questions[self.current]
            self.quiz_label.config(text=kana)
            self.entry.delete(0, tk.END)
        else:
            self.end_quiz()

    def check_answer(self):
        user_answer = self.entry.get().strip().lower()
        kana, romaji = self.questions[self.current]

        if user_answer == romaji:
            messagebox.showinfo("Your answer is correct!")
            self.correct += 1
        else:
            messagebox.showinfo("Your answer is incorrect.", f"It should be '{romaji}'.")
            self.incorrect += 1

        self.current += 1
        self.next_question()

    def end_quiz(self):
        total = self.correct + self.incorrect
        messagebox.showinfo(
            "This is the end of the quiz.",
            f"よくできました! You have answered {self.correct} out of {total} questions correctly 🌟"
        )
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = KanaQuizGUI(root)
    root.mainloop()