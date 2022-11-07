import tkinter as tk
from tkinter import filedialog

from algorithms.task3.longest_subsequence import lcs


class TextMatcher:
    def __init__(self, frame: tk.Frame, side: str):
        self.frame = tk.Frame(frame)
        self.frame.pack(side=side, fill=tk.BOTH, expand=True)

        self.load_button = tk.Button(self.frame, text=f"Load left {side}", command=self.load_file)
        self.load_button.pack(fill=tk.BOTH, expand=True, side="top")

        self.text_window = tk.Text(self.frame, width=50, height=20)
        self.text_window.pack(side="bottom", fill=tk.BOTH, expand=True)
        self.text_window.tag_config("match", background="green", foreground="black")
        self.text_window.tag_config("no_match", background="red", foreground="black")
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


class Gui(tk.Frame):
    """
    Class for loading two files and displaying they content, one
    file in the left text widget and the other in the right text widget.

    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        buttons_frame = tk.Frame(root)
        buttons_frame.pack(side=tk.TOP, expand=True, fill=tk.X)

        self.texts = [
            TextMatcher(buttons_frame, "left"),
            TextMatcher(buttons_frame, "right"),
        ]

        self.scrollbar = tk.Scrollbar(buttons_frame, orient=tk.VERTICAL, command=self.scroll)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.texts[0].text_window["yscrollcommand"] = self.scrollbar.set
        self.texts[1].text_window["yscrollcommand"] = self.scrollbar.set

        self.search_button = tk.Button(self.master, text="Search", command=self.search)
        self.search_button.pack(side=tk.BOTTOM)

    def scroll(self, *args):
        for text in self.texts:
            text.text_window.yview(*args)

    def search(self):
        subsequences = lcs(self.texts[0].raw_text, self.texts[1].raw_text)

        longer_text, shorter_text = (
            (self.texts[0], self.texts[1])
            if len(self.texts[0].raw_text) > len(self.texts[1].raw_text)
            else (self.texts[1], self.texts[0])
        )
        shorter_iter = iter(shorter_text.raw_text)

        for text in self.texts:
            text.clear()

        for i, raw_line in enumerate(longer_text.raw_text):
            if raw_line in subsequences:
                seq = subsequences.pop(0)

                while True:
                    next_ = next(shorter_iter)

                    if next_ != seq:
                        shorter_text.insert(next_, "no_match")
                        longer_text.insert("")
                    else:
                        shorter_text.insert(next_, "match")
                        longer_text.insert(raw_line, "match")
                        break

            else:
                longer_text.insert(raw_line, "no_match")
                shorter_text.insert("")

        for other_iter in shorter_iter:
            shorter_text.insert(other_iter, "no_match")


if __name__ == "__main__":
    root = tk.Tk()
    app = Gui(master=root)
    app.mainloop()
