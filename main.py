import time
from datetime import datetime
import random

# Function to display the current date and time
def display_date_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"The current date & time is(今の日付と時刻は): {dt_string}")

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

    hira_list = [(hira, romaji) for romaji, hira, kata in kana_romanji]
    kata_list = [(kata, romaji) for romaji, hira, kata in kana_romanji]
    return hira_list, kata_list

# Function to display the Kana lists
def list_display():
    hira_list, kata_list = kana_list()
    print(f"{'Romaji':<10} {'Hiragana':<10} {'Katakana':<10}")
    print("-" * 30)
    for hira, romaji in hira_list:
        kata = next((k for k, r in kata_list if r == romaji), "")
        print(f"{romaji:<10} {hira:<10} {kata:<10}")

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

    def display_score(self, correct, total):
        percent = (correct / total) * 100
        print(f"\nYou got {correct} out of {total} correct.")
        print(f"Score: {percent:.1f}%")
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

# Main function of the program
def main():
    # Welcome message & ask for the user's name
    display_date_time()
    print("Hello, welcome to the Hiragana & Katakana game.こんにちは、ひらがなとカタカナのゲームへようこそ。")
    name = input("(お名前は何ですか？)What is your name? ").strip()
    time.sleep(0.5)
    print("Hello,", name.title(), ".")
    print("こんにちは、" + name.title() + "さん。")
    time.sleep(0.5)
    
    