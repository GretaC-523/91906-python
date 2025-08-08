import tkinter as tk

class KanaQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kana Quiz")
        self.root.geometry("700x400")
        self.root.configure(bg="#1e1e1e")  # Dark mode background

        # Color settings
        self.bg_color = "#1e1e1e"
        self.fg_color = "#ffffff"
        self.button_color = "#3c3f41"

        # Kana lists
        self.hiragana_list = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ"]
        self.katakana_list = ["ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ"]

        self.init_welcome_screen()

    def init_welcome_screen(self):
        # Clear screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title label
        title = tk.Label(
            self.root, text="Welcome to Kana Quiz!",
            font=("Comic Sans MS", 20, "bold"),
            bg=self.bg_color, fg=self.fg_color
        )
        title.pack(pady=30)

        # Subtitle label
        subtitle = tk.Label(
            self.root, text="Choose a mode to begin:\nモードを選んでください",
            font=("Comic Sans MS", 14),
            bg=self.bg_color, fg=self.fg_color
        )
        subtitle.pack(pady=10)

        # Initialize buttons
        self.init_buttons()

    def init_buttons(self):
      button_frame = tk.Frame(self.root, bg=self.bg_color)
      button_frame.pack(pady=30)

      # Hiragana button (top-left)
      self.hiragana_button = tk.Button(
      button_frame, text="Hiragana ひらがな", width=20, height=2,
      font=("Trebuchet MS", 12), command=self.start_hiragana_quiz,
      bg="#ff49ed", fg="#1e1e1e"
    )
      self.hiragana_button.grid(row=0, column=0, padx=10, pady=5)

      # Katakana button (top-right)
      self.katakana_button = tk.Button(
      button_frame, text="Katakana カタカナ", width=20, height=2,
      font=("Trebuchet MS", 12), command=self.start_katakana_quiz,
      bg="#ff49ed", fg="#1e1e1e"
    )
      self.katakana_button.grid(row=0, column=1, padx=10, pady=5)

    # Both button (centered below)
      self.both_button = tk.Button(
      button_frame, text="Both ひらがな と カタカナ", width=44, height=2,
      font=("Trebuchet MS", 12), command=self.start_both_quiz,
      bg="#ff49ed", fg="#1e1e1e"
    )
      self.both_button.grid(row=1, column=0, columnspan=2, pady=10)

    def display_kana_list(self, kana_list, title_text):
        # Clear screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title
        title = tk.Label(
            self.root, text=title_text,
            font=("Comic Sans MS", 18, "bold"),
            bg=self.bg_color, fg=self.fg_color
        )
        title.pack(pady=20)

        # Kana display
        kana_frame = tk.Frame(self.root, bg=self.bg_color)
        kana_frame.pack(pady=10)

        for kana in kana_list:
            label = tk.Label(
                kana_frame, text=kana,
                font=("Comic Sans MS", 16),
                bg=self.bg_color, fg=self.fg_color,
                width=4, height=2
            )
            label.pack(side="left", padx=5)

        # Back button
        back_button = tk.Button(
            self.root, text="Back 戻る", width=15, height=2,
            font=("Comic Sans MS", 12), command=self.init_welcome_screen,
            bg=self.button_color, fg=self.fg_color
        )
        back_button.pack(pady=20)

    def start_hiragana_quiz(self):
        self.display_kana_list(self.hiragana_list, "Hiragana Quiz ひらがな")

    def start_katakana_quiz(self):
        self.display_kana_list(self.katakana_list, "Katakana Quiz カタカナ")

    def start_both_quiz(self):
        combined = self.hiragana_list + self.katakana_list
        self.display_kana_list(combined, "Both Quiz ひらがな と カタカナ")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = KanaQuizApp(root)
    root.mainloop()