import tkinter as tk

from algorithms.task3.longest_subsequence import lcs_with_cached_table
from algorithms.task3.match_enum import MatchEnum
from algorithms.task3.view.textmatcher import TextMatcher


class Gui(tk.Frame):
    """
    Class for loading two files and displaying they content, one
    file in the left text widget and the other in the right text widget.

    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        frame = tk.Frame(master)
        frame.pack(side=tk.TOP, expand=True, fill=tk.X)

        self.texts = [
            TextMatcher(frame, "left"),
            TextMatcher(frame, "right"),
        ]

        self.scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.scroll)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.texts[0].text_window["yscrollcommand"] = self.scrollbar.set
        self.texts[1].text_window["yscrollcommand"] = self.scrollbar.set

        self.search_button = tk.Button(self.master, text="Search", command=self.search)
        self.search_button.pack(side=tk.BOTTOM)

    def reset_state(self):
        for text in self.texts:
            text.reset_state()

    def scroll(self, *args):
        for text in self.texts:
            text.text_window.yview(*args)

    def search(self):
        subsequences = lcs_with_cached_table(self.texts[0].raw_text, self.texts[1].raw_text)

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
                        shorter_text.insert(f"-{next_}", MatchEnum.NO_MATCH)
                        longer_text.insert("", MatchEnum.NO_MATCH)
                    else:
                        shorter_text.insert(f"+{next_}", MatchEnum.MATCH)
                        longer_text.insert(f"+{raw_line}", MatchEnum.MATCH)
                        break
            else:
                longer_text.insert(f"-{raw_line}", MatchEnum.NO_MATCH)
                shorter_text.insert("", MatchEnum.NO_MATCH)

        for other_el in shorter_iter:
            shorter_text.insert(f"-{other_el}", MatchEnum.NO_MATCH)
