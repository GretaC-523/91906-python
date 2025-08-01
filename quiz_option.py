import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random
import time

# Function to display Kana options
def show_quiz_options(self):
        self.welcome_frame.destroy()

        self.option_frame = tk.Frame(self.master)
        self.option_frame.pack(expand=True)

        label = tk.Label(self.option_frame, text="Choose quiz type: ", font=("Helvetica", 14))
        label.pack(pady=10)

        tk.Button(self.option_frame, text="Hiragana ひらがな", command=self.start_hiragana).pack(pady=5)
        tk.Button(self.option_frame, text="Katakana カタカナ", command=self.start_katakana).pack(pady=5)
        tk.Button(self.option_frame, text="Both ひらがな と カタカナ", command=self.start_both).pack(pady=5)
