import time
from datetime import datetime

# Function to display the current date and time
def display_date_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"The current date & time is/今の日付と時刻は: {dt_string}")

# Welcome message & ask for the user's name
display_date_time()
print("Hello, welcome to the Hiragana & Katakana game.こんにちは、ひらがなとカタカナのゲームへようこそ。")
name = input("(お名前は何ですか？)What is your name? ").strip()
time.sleep(0.5)
print("Hello,", name.title(), ".")
print("こんにちは、" + name.title() + "さん。") 

# Hiragana and Katakana lists
 def kana_list():
     # Hiragana
     hiragana = [
         "あ", "い", "う", "え", "お",  # a, i, u, e, o
         "か", "き", "く", "け", "こ",  # ka, ki, ku, ke, ko
         "さ", "し", "す", "せ", "そ",  # sa, shi, su, se, so
         "た", "ち", "つ", "て", "と",  # ta, chi, tsu, te, to
         "な", "に", "ぬ", "ね", "の",  # na, ni, nu, ne, no
         "は", "ひ", "ふ", "へ", "ほ",  # ha, hi, fu, he, ho
         "ま", "み", "む", "め", "も",  # ma, mi, mu, me, mo
         "や", "ゆ", "よ",              # ya, yu, yo
         "ら", "り", "る", "れ", "ろ",  # ra, ri, ru, re, ro
         "わ", "を", "ん"               # wa, wo, n
         "きゃ", "きゅ", "きょ",        # kya, kyu, kyo
         "しゃ", "しゅ", "しょ",        # sha, shu, sho
         "ちゃ", "ちゅ", "ちょ",        # cha, chu, cho
         "にゃ", "にゅ", "にょ",        # nya, nyu, nyo
         "ひゃ", "ひゅ", "ひょ",        # hya, hyu, hyo
         "みゃ", "みゅ", "みょ",        # mya, myu, myo
         "りゃ", "りゅ", "りょ",        # rya, ryu, ryo
         "ぎゃ", "ぎゅ", "ぎょ",        # gya, gyu, gyo
         "じゃ", "じゅ", "じょ",        # ja, ju, jo
         "びゃ", "びゅ", "びょ",        # bya, byu, byo
         "ぴゃ", "ぴゅ", "ぴょ"         # pya, pyu, pyo
 ]
 
 # Katakana
 katakana = [
     "ア", "イ", "ウ", "エ", "オ",  # a, i, u, e, o
     "カ", "キ", "ク", "ケ", "コ",  # ka, ki, ku, ke, ko
     "サ", "シ", "ス", "セ", "ソ",  # sa, shi, su, se, so
     "タ", "チ", "ツ", "テ", "ト",  # ta, chi, tsu, te, to
     "ナ", "ニ", "ヌ", "ネ", "ノ",  # na, ni, nu, ne, no
     "ハ", "ヒ", "フ", "ヘ", "ホ",  # ha, hi, fu, he, ho
     "マ", "ミ", "ム", "メ", "モ",  # ma, mi, mu, me, mo
     "ヤ", "ユ", "ヨ",              # ya, yu, yo
     "ラ", "リ", "ル", "レ", "ロ",  # ra, ri, ru, re, ro
     "ワ", "ヲ", "ン"               # wa, wo, n
     "キャ", "キュ", "キョ",        # kya, kyu, kyo
     "シャ", "シュ", "ショ",        # sha, shu, sho
     "チャ", "チュ", "チョ",        # cha, chu, cho
     "ニャ", "ニュ", "ニョ",        # nya, nyu, nyo
     "ヒャ", "ヒュ", "ヒョ",        # hya, hyu, hyo
     "ミャ", "ミュ", "ミョ",        # mya, myu, myo
     "リャ", "リュ", "リョ",        # rya, ryu, ryo
     "ギャ", "ギュ", "ギョ",        # gya, gyu, gyo
     "ジャ", "ジュ", "ジョ",        # ja, ju, jo
     "ビャ", "ビュ", "ビョ",        # bya, byu, byo
     "ピャ", "ピュ", "ピョ"         # pya, pyu, pyo   
 ]

class Quiz_selections:
 # Ask if the user wants to start the quiz or not and if they want to see the lists
 def start_quiz():
     start = input("Do you want to start the quiz now/need some more time? (yes/no): ").strip().lower()
     if start == 'yes' or 'y':
         quiz_method()
     else:
         print("Thank you for visiting! ありがとうございました。")
     choice = input("Do you want to see the Hiragana & Katakana lists? (yes/no): ").strip().lower()
    
     if choice == 'yes' or 'y':
         kana_list()
    
     elif choice == 'no' or 'n':
         print("You may start the quiz when you are ready. いつでも準備した後で、クイズを始めることができます。")
         print("Good luck! 頑張ります！") 
