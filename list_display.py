import tkinter as tk

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

# Function to display the Kana lists in a new window
def display_kana_lists(self):
    list_window = tk.Toplevel(self.master)
    list_window.title("Kana List")
    list_window.configure(bg="#1e1e1e")

    title = tk.Label(list_window, text="Kana List", font=("Comic Sans MS", 16, "bold"),
                     fg="white", bg="#1e1e1e")
    title.pack(pady=10)

    # Create a grid frame
    grid_frame = tk.Frame(list_window, bg="#1e1e1e")
    grid_frame.pack(padx=20, pady=10)

    # Header row
    headers = ["Romaji", "Hiragana", "Katakana"]
    for col, text in enumerate(headers):
        tk.Label(grid_frame, text=text, font=("Comic Sans MS", 14, "bold"),
                 fg="#00ffff", bg="#1e1e1e", padx=10).grid(row=0, column=col)

    # Combine hiragana and katakana lists
    full_list = []
    for hira, romanji in self.hiragana:
        kata = next((k for k, r in self.katakana if r == romanji), "")
        full_list.append((romanji, hira, kata))

    # Display all kana in grid
    for row, (romanji, hira, kata) in enumerate(full_list, start=1):
        tk.Label(grid_frame, text=romanji, font=("Comic Sans MS", 12),
                 fg="white", bg="#1e1e1e", padx=10).grid(row=row, column=0)
        tk.Label(grid_frame, text=hira, font=("Comic Sans MS", 12),
                 fg="white", bg="#1e1e1e", padx=10).grid(row=row, column=1)
        tk.Label(grid_frame, text=kata, font=("Comic Sans MS", 12),
                 fg="white", bg="#1e1e1e", padx=10).grid(row=row, column=2)

    # Back button
    back_btn = tk.Button(list_window, text="Back", font=("Comic Sans MS", 12),
                         bg="#444", fg="white", command=list_window.destroy)
    back_btn.pack(pady=10)
