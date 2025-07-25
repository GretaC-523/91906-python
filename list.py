import time

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

    print("Kana List with romanji:")
    time.sleep(1)
    print(f"{'Romaji':<50} {'Hiragana':<50} {'Katakana':<50}")
    print("-" * 150)
    for romaji, hira, kata in kana_romanji:
        print(f"{romaji:<50} {hira:<50} {kata:<50}")

if __name__ == "__main__":
    kana_list() 