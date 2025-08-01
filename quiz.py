import time
import random
import tkinter as tk
from tkinter import messagebox

# Class function of the Kana quiz
class Kana_quiz: 
    def __init__(self):
        self.hira_list, self.kata_list = kana_list()

    # Asks the user to choose between Hiragana or Katakana quiz
    def quiz_choice(self):
        choice = input("Which quiz would you like to take? (hiragana/katakana/both): ").strip().lower()
        if choice in ['hiragana', 'ひらがな', '平仮名']:
            self.run_quiz(self.hira_list, "Hiragana")
        elif choice in ['katakana', 'カタカナ', '片仮名']:
            self.run_quiz(self.kata_list, "Katakana")
        elif choice == 'both':
            self.run_quiz(self.hira_list, "Hiragana")
            self.run_quiz(self.kata_list, "Katakana")
        else:
            print("Please enter either 'hiragana', 'katakana', or 'both'.")
            self.start()

    # Function of the Hiragana quiz
    def run_quiz(self, kana_set, label):
        print(f"Starting {label} quiz...")
        time.sleep(1)
        score = 0
        questions = random.sample(kana_set, 10)
        for kana, romaji in questions:
            user_input = input(f"What is the romaji for {kana}? ").strip().lower()
            if user_input == romaji:
                score += 1
                print("Correct! 👍")
            else:
                print(f"Oops! The correct answer is {romaji}.")
                time.sleep(0.5)
        self.display_score(score, len(questions))
    
    # Function to display the user's score
    def display_score(self, correct, total):
        percent = (correct / total) * 100
        print(f"\nYou got {correct} out of {total} correct.")
        print(f"Score: {percent:.1f}")
        time.sleep(1) 

        if correct == 0:
            print("全ての答えが間違っていました。復習してからもう一度挑戦しましょう！")
            print("You did not answer any questions correctly. Please try again after revision.")
        elif correct < total / 2:
            print("半分未満正解でした。頑張ってください！")
            print("You answered less than half of the questions correctly. Keep trying!")
        elif correct == total / 2:
            print("よくできました！あと少しで満点です！")
            print("You answered half of the questions correctly. Good job! Almost there!")
        elif correct == total:
            print("満点です！おめでとうございます！")
            print("Congratulations! You answered all questions correctly!")

        print("Thank you for taking the quiz! Goodbye! クイズをしてくれてありがとうございました! さよなら。")