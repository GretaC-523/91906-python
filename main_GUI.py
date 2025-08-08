# Author: Greta
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random
import time

# Kana List display function
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
    hiragana = [(hira, romaji) for romaji, hira, kata in kana_romanji]
    katakana = [(kata, romaji) for romaji, hira, kata in kana_romanji]
    return hiragana, katakana

# GUI Quiz Class function
class KanaQuizGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Kana Quiz 🌸")
        self.master.geometry("500x400")

        self.hiragana, self.katakana = kana_list()
        self.questions = []
        self.current = 0
        self.correct = 0

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.master)
        self.welcome_frame.pack(expand=True)

        welcome_label = tk.Label(
            self.welcome_frame,
            text="Welcome to the Kana quiz.\nひらがなとカタカナのゲームへようこそ。",
            font=("Meiryo", 14, "bold"),
            fg="#4B0082",
            pady=10
        )
        welcome_label.pack()

        now = datetime.now()
        date_time_label = tk.Label(
            self.welcome_frame,
            text=now.strftime("The current date & time is / 今の日付と時刻は: %A, %d %B %Y\n⏰%I:%M %p"),
            font=("Meiryo", 10),
            fg="#555555",
            pady=10
        )
        date_time_label.pack()

        start_button = tk.Button(
            self.welcome_frame,
            text="Start Quiz",
            font=("Trebuchet MS", 14),
            bg="#90EE90",
            command=self.show_quiz_options
        )
        start_button.pack(pady=5)

        list_button = tk.Button(
            self.welcome_frame,
            text="View Kana List",
            font=("Trebuchet MS", 12),
            bg="#ADD8E6",
            command=self.display_kana_lists
        )
        list_button.pack(pady=5)
     
    # Function to display the Kana lists in a new window
    def display_kana_lists(self):
        list_window = tk.Toplevel(self.master)
        list_window.title("Kana List")
        list_window.geometry("400x500")

        text = tk.Text(list_window, wrap="none", font=("Comic Sans MS", 12))
        text.pack(expand=True, fill="both")

        text.insert("end", f"{'Romanji':<10} {'Hiragana':<10} {'Katakana':<10}\n")
        text.insert("end", "-" * 30 + "\n")

        for hira, romanji in self.hiragana:
            kata = next((k for k, r in self.katakana if r == romanji), "")
            text.insert("end", f"{romanji:<10} {hira:<10} {kata:<10}\n")
    
    # Show quiz options for Hiragana, Katakana, or Both
    def show_quiz_options(self):
        self.welcome_frame.destroy()

        self.option_frame = tk.Frame(self.master)
        self.option_frame.pack(expand=True)

        label = tk.Label(self.option_frame, text="Choose quiz type: ", font=("Courier New", 14))
        label.pack(pady=10)

        tk.Button(self.option_frame, text="Hiragana ひらがな",
          command=self.start_hiragana,
          bg="#ff94ed", font=("Trebuchet MS", 14, "bold")).pack(pady=5)

        tk.Button(self.option_frame, text="Katakana カタカナ",
          command=self.start_katakana,
          bg="#FF94ed", font=("Trebuchet MS", 14, "bold")).pack(pady=5)

        tk.Button(self.option_frame, text="Both ひらがな と カタカナ",
          command=self.start_both,
          bg="#FF94ed", font=("Trebuchet MS", 14, "bold")).pack(pady=5)

    # Start the quiz with the chosen option
    def start_quiz(self, question_set):
        self.option_frame.destroy()
        self.questions = random.sample(question_set, 10)
        self.current = 0
        self.correct = 0

        self.quiz_label = tk.Label(self.master, text="", font=("Courier New", 24))
        self.quiz_label.pack(pady=20)

        self.entry = tk.Entry(self.master, font=("Courier New", 14))
        self.entry.pack()

        self.submit_btn = tk.Button(self.master, text="Submit", command=self.check_answer)
        self.submit_btn.config(font=("Trebuchet MS", 12), bg="#A7A8FF", fg="#000000")
        self.submit_btn.pack(pady=10)

        self.next_question()

    def start_hiragana(self):
        self.start_quiz(self.hiragana)

    def start_katakana(self):
        self.start_quiz(self.katakana)

    def start_both(self):
        self.start_quiz(self.hiragana + self.katakana)

    def next_question(self):
        if self.current < len(self.questions):
            kana, _ = self.questions[self.current]
            self.quiz_label.config(text=kana)
            self.quiz_label.configure(fg="Meiryo", bg="#F0F8FF")
            self.entry.delete(0, tk.END)
        else:
            self.show_results()
     
    def check_answer(self):
     user_input = self.entry.get().strip().lower()
     if not (2 <= len(user_input) <= 3):
            self.feedback_label.config(text="Please enter 2-3 characters.", fg=self.colors['warning'])
     elif user_input == self.correct_answer:
            self.feedback_label.config(text="Correct! 正解です！", fg=self.colors['correct'])
     else:
            self.feedback_label.config(text=f"Incorrect. The answer is '{self.correct_answer}' .", fg=self.colors['incorrect'])

     self.current += 1
     self.next_question()
    
    # Show the final results(scores) after the quiz ends
    def show_results(self):
        total = len(self.questions)
        score_msg = f"You have answered {self.correct} out of {total} questions correctly.\n"
        score_msg.configure(fg="Courier New", bg="#F0F8FF")
        messagebox.showinfo("This is the end of the quiz", score_msg)
        messagebox.configure(fg="Courier New", bg="#F0F8FF")
        self.master.quit()

# Launch the GUI application 
if __name__ == "__main__":
    root = tk.Tk()
    KanaQuizGUI(root)
    root.mainloop()
