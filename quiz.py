import time
import random
from list import kana_list
from quiz_score import QuizScore

# Ask the user about the quiz type & if they want to see the lists/start the quiz
def start_quiz():
 start = input("Do you want to start the quiz now/need some more time? (start/not yet): ").strip().lower()
 if start == 'start':
     Kana_quiz().quiz_method()
 elif start == 'not yet': 
     list_choice = input("Do you want to see the Kana lists? (yes/no): ").strip().lower()
     if list_choice == 'yes' or list_choice == 'y':
         kana_list()
         print("Good luck with your revision! 復習を頑張ります！") 

     elif list_choice == 'no' or list_choice == 'n':
         print("You may start the quiz when you are ready. 準備した後で、クイズを始めることができます。")
         print("Good luck! 頑張ります！") 

# Class function of the Kana quiz
class Kana_quiz: 
    # Asks the user to choose between Hiragana or Katakana quiz
    def quiz_method(self):
        choice = input("Which quiz would you like to take? (hiragana/katakana): ").strip().lower()
        if choice == 'hiragana' or choice == 'ひらがな' or choice == '平仮名':
            self.hiragana()
        elif choice == 'katakana' or choice == 'カタカナ' or choice == '片仮名':
            self.katakana()
        else:
            print("Invalid choice. Please choose either 'hiragana' or 'katakana'.")
            self.quiz_method()
    
    # Function of the Hiragana quiz  
    def hiragana(self):
     print("Starting Hiragana quiz...")
     time.sleep(1) 
     score = QuizScore(0, 10)
     questions = random.sample(kana_list()[0], 10)  # Randomly select 10 Hiragana
     for question, answer in questions:
         user_answer = input(f"What is the romanji for {question}? ")
         if user_answer.lower() == answer:
             score += 10
             print("Correct!")
         else:
             print(f"Oops! The answer should be {answer}.")
             time.sleep(1)
     score.score_display()

    # Function of the Katakana quiz
    def katakana(self): 
     print("Starting Katakana quiz...")
     time.sleep(1)
     score = QuizScore(0, 10)
     questions = random.sample(kana_list()[1], 10)  # Randomly select 10 Katakana
     for question, answer in questions:
         user_answer = input(f"What is the romanji for {question}? ")
         if user_answer.lower() == answer:
             score += 10
             print("Correct!")
         else:
             print(f"Oops! The answer should be {answer}.")
             time.sleep(1) 
     score.score_display()
