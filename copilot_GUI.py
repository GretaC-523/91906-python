# author: Greta
import random
import tkinter as tk
from tkinter import messagebox
from list import kana_list
from quiz_score import QuizScore

class KanaQuizGUI:
    def __init__(self, master):
        self.master = master
        master.title("Kana Quiz 🌸")
        self.hiragana, self.katakana = kana_list()
        self.questions = []
        self.score = QuizScore()
        self.current = 0

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
        self.start_quiz(self.hiragana)

    def start_katakana(self):
        self.start_quiz(self.katakana)

    def start_both(self):
        self.start_quiz(self.hiragana + self.katakana)

    def start_quiz(self, question_list):
        self.questions = random.sample(question_list, 10)
        self.score.reset()
        self.current = 0
        self.label.pack_forget()
        self.hira_btn.pack_forget()
        self.kata_btn.pack_forget()
        self.both_btn.pack_forget()
        self.quiz_label.pack()
        self.entry.pack()
        self.submit_btn.pack()
        self.next_question()

    def next_question(self):
        self.entry.delete(0, tk.END)
        if self.current < len(self.questions):
            kana, romaji = self.questions[self.current]
            self.correct_answer = romaji
            self.quiz_label.config(text=kana)
        else:
            self.end_quiz()

    def check_answer(self):
        user_answer = self.entry.get().strip().lower()
        if user_answer == self.correct_answer:
            messagebox.showinfo("Result", "Correct! 🎉")
            self.score.correct()
        else:
            messagebox.showinfo("Result", f"Incorrect! The answer is '{self.correct_answer}'.")
            self.score.incorrect()
        self.current += 1
        self.next_question()

    def end_quiz(self):
        self.quiz_label.pack_forget()
        self.entry.pack_forget()
        self.submit_btn.pack_forget()
        final_score = self.score.get_score()
        messagebox.showinfo("Quiz Completed", f"You scored: {final_score}/10")
        self.reset_ui()

    def reset_ui(self):
        self.label.pack()
        self.hira_btn.pack()
        self.kata_btn.pack()
        self.both_btn.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = KanaQuizGUI(root)
    root.mainloop()