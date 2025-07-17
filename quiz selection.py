import time
import list
import kana quiz

# To ask the user about the quiz type & if they want to see the lists/start the quiz
class Quiz_selections:
 # Ask if the user wants to start the quiz or not & if they want to see the lists
 def start_quiz():
     start = input("Do you want to start the quiz now/need some more time? (yes/no): ").strip().lower()
     if start == 'yes' or 'y':
         quiz_type()
     else:
         list_choice = input("Do you want to see the Hiragana & Katakana lists? (yes/no): ").strip().lower()
         if list_choice == 'yes' or 'y':
             kana_list()

         elif list_choice == 'no' or 'n':
             print("You may start the quiz when you are ready. 準備した後で、クイズを始めることができます。")
             print("Good luck! 頑張ります！") 
 
 # Ask the user if they want to do only 1 Kana quiz/both
 def quiz_type():
     # Ask the user if they want to do either 1 of the Kanas/both
     type_choice = input("Do you want to do Hiragana, Katakana, or both? (hiragana/katakana/both): ").strip().lower()
        if type_choice == 'hiragana' or 'hira' or 'ひらがな' or '平仮名':
         kana_quiz.hiragana()

        elif type_choice == 'katakana' or 'kata' or 'カタカナ' or '片仮名':
         kana_quiz.katakana()

        elif type_choice == 'both':
         kana_quiz()

        else:
         print("Invalid input. Please answer with either one of these options:")
         print("'hiragana', 'katakana', 'hira', 'kata', 'ひらがな', 'カタカナ', '平仮名', '片仮名', 'both'")
         quiz_type()  # Ask the question again

