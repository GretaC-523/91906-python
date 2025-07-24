import time
from datetime import datetime
import random

# Function to display the current date and time
def display_date_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"The current date & time is(今の日付と時刻は): {dt_string}")

# Welcome message & ask for the user's name
display_date_time()
print("Hello, welcome to the Hiragana & Katakana game.こんにちは、ひらがなとカタカナのゲームへようこそ。")
name = input("(お名前は何ですか？)What is your name? ").strip()
time.sleep(0.5)
print("Hello,", name.title(), ".")
print("こんにちは、" + name.title() + "さん。")

# Hiragana and Katakana lists with romaji
def kana_list():
    kana_romanji = [
        ("a", "あ", "ア"), ("i", "い", "イ"), ("u", "う", "ウ"), ("e", "え", "エ"), ("o", "お", "オ"),
        ("ka", "か", "カ"), ("ki", "き", "キ"), ("ku", "く", "ク"), ("ke", "け", "ケ"), ("ko", "こ", "コ"),
        ("sa", "さ", "サ"), ("shi", "し", "シ"), ("su", "す", "ス"), ("se", "せ", "セ"), ("so", "そ", "ソ"),
        ("ta", "た", "タ"), ("chi", "ち", "チ"), ("tsu", "つ", "ツ"), ("te", "て", "テ"), ("to", "と", "ト"),
        ("na", "な", "ナ"), ("ni", "に", "ニ"), ("nu", "ぬ", "ヌ"), ("ne", "ね", "ネ"), ("no", "の", "ノ"),
        ("ha", "は", "ハ"), ("hi", "ひ", "ヒ"), ("fu", "ふ", "フ"), ("he", "へ", "ヘ"), ("ho", "ほ", "ホ"),
        ("ma", "ま", "マ"), ("mi", "み", "ミ"), ("mu", "む", "ム"), ("me", "め", "メ"), ("mo", "も", "モ"),
        ("ya", "や", "ヤ"), ("yu", "ゆ", "ユ"), ("yo", "よ", "ヨ"),
        ("ra", "ら", "ラ"), ("ri", "り", "リ"), ("ru", "る", "ル"), ("re", "れ", "レ"), ("ro", "ろ", "ロ"),
        ("wa", "わ", "ワ"), ("wo", "を", "ヲ"), ("n", "ん", "ン"),
        ("kya", "きゃ", "キャ"), ("kyu", "きゅ", "キュ"), ("kyo", "きょ", "キョ"),
        ("sha", "しゃ", "シャ"), ("shu", "しゅ", "シュ"), ("sho", "しょ", "ショ"),
        ("cha", "ちゃ", "チャ"), ("chu", "ちゅ", "チュ"), ("cho", "ちょ", "チョ"),
        ("nya", "にゃ", "ニャ"), ("nyu", "にゅ", "ニュ"), ("nyo", "にょ", "ニョ"),
        ("hya", "ひゃ", "ヒャ"), ("hyu", "ひゅ", "ヒュ"), ("hyo", "ひょ", "ヒョ"),
        ("mya", "みゃ", "ミャ"), ("myu", "みゅ", "ミュ"), ("myo", "みょ", "ミョ"),
        ("rya", "りゃ", "リャ"), ("ryu", "りゅ", "リュ"), ("ryo", "りょ", "リョ"),
        ("gya", "ぎゃ", "ギャ"), ("gyu", "ぎゅ", "ギュ"), ("gyo", "ぎょ", "ギョ"),
        ("ja", "じゃ", "ジャ"), ("ju", "じゅ", "ジュ"), ("jo", "じょ", "ジョ"),
        ("bya", "びゃ", "ビャ"), ("byu", "びゅ", "ビュ"), ("byo", "びょ", "ビョ"),
        ("pya", "ぴゃ", "ピャ"), ("pyu", "ぴゅ", "ピュ"), ("pyo", "ぴょ", "ピョ")
    ]

    print("Kana List with romaji:")
    time.sleep(1)
    print(f"{'Romaji':<50} {'Hiragana':<50} {'Katakana':<50}")
    print("-" * 150)
    for romaji, hira, kata in kana_romanji:
        print(f"{romaji:<50} {hira:<50} {kata:<50}")

if __name__ == "__main__":
    kana_list()

# Ask the user about the quiz type & if they want to see the lists/start the quiz
def start_quiz():
 start = input("Do you want to start the quiz now/need some more time? (yes/no): ").strip().lower()
 if start == 'yes' or start == 'y':
     Kana_quiz()
 else:
     list_choice = input("Do you want to see the Hiragana & Katakana lists? (yes/no): ").strip().lower()
     if list_choice == 'yes' or list_choice == 'y':
         kana_list()
     elif list_choice == 'no' or list_choice == 'n':
         print("You may start the quiz when you are ready. 準備した後で、クイズを始めることができます。")
         print("Good luck! 頑張ります！")

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

# Class function to display the quiz score
class QuizScore():
    def __init__(self, correct_answers, total_questions):
        self.correct_answers = correct_answers
        self.total_questions = total_questions

    def display(self):
        print(f"You have answered {self.correct_answers} out of {self.total_questions} questions correctly.")
        score = (self.correct_answers / self.total_questions) * 100
        print(f"Your quiz score is: {score}%")
        time.sleep(1)
        print("Thank you for taking the quiz! Goodbye! クイズをしてくれてありがとうございました! さよなら。") 

        if score == 0:
            print("You did not answer any questions correctly. Please try again after revision.")
            print("Good luck for next time!")
            return

        elif score < 50 and score > 0:
            print("You answered less than half of the questions correctly. Please try again after revision.")
            print("Good luck for next time!")
            return

        elif score > 50 and score <= 90:
            print("You answered more than half of the questions correctly. Good job! よくできました！")
            print("Keep practicing to get full marks!")
            return

        elif score == 100:
            print("Congratulations! You answered all questions correctly.")
            print("おめでとうございます！ よくできました。")
