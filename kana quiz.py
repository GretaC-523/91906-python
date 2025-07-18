import time
import random
from list import kana_list
hiragana, katakana = kana_list()   

# Importing the QuizScore class from quiz-score.py
from quiz_score import display_score as QuizScore 

# Class function of the Kana quiz
class Kana_quiz: 
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
     score.display()

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
     score.display()  
    
if __name__ == "__main__":
 quiz = Kana_quiz()
 while True:
     choice = input("Choose a quiz: 1 for Hiragana, 2 for Katakana, or 'exit' to quit: ")
     if choice == '1':
         quiz.hiragana()
     elif choice == '2':
         quiz.katakana()
     elif choice.lower() == 'exit':
         print("This is the end of the quiz.")
         break
     else:
         print("Invalid choice. Please try again.")

