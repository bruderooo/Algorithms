import tkinter as tk

from algorithms.task3.view.gui import Gui

if __name__ == "__main__":
    root = tk.Tk()
    app = Gui(master=root)
    app.mainloop()
