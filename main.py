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
