import tkinter as tk
from tkinter import filedialog

from algorithms.task3.match_enum import MatchEnum


class TextMatcher:
    def __init__(self, frame: tk.Frame, side: str):
        self.frame = tk.Frame(frame)
        self.frame.pack(side=side, fill=tk.BOTH, expand=True)

        self.load_button = tk.Button(self.frame, text=f"Load left {side}", command=self.load_file)
        self.load_button.pack(fill=tk.BOTH, expand=True, side="top")

        self.text_window = tk.Text(self.frame, width=50, height=20)
        self.text_window.pack(side="bottom", fill=tk.BOTH, expand=True)
        self.text_window.tag_config(MatchEnum.MATCH, background="green", foreground="black")
        self.text_window.tag_config(MatchEnum.NO_MATCH, background="red", foreground="black")
        self.raw_text = None

    def load_file(self):
        file_path = filedialog.askopenfilename()

        with open(file_path, "r") as file:
            self.text_window.configure(state="normal")
            self.text_window.delete(1.0, tk.END)
            readed_file = file.read()
            self.insert(readed_file)
            self.raw_text = readed_file.splitlines()

    def insert(self, text: str, tag: str = None):
        self.text_window.configure(state="normal")
        self.text_window.insert(tk.END, f"{text}\n".encode("UTF-8"), tag)
        self.text_window.configure(state="disabled")

    def clear(self):
        self.text_window.configure(state="normal")
        self.text_window.delete(1.0, tk.END)
        self.text_window.configure(state="disabled")

    def reset_state(self):
        self.text_window.configure(state="normal")
        self.text_window.delete(1.0, tk.END)
        self.insert("".join(self.raw_text))
