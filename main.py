import tkinter as tk
from tkinter import ttk

from setter import Control
from output import Screen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("toy example")
        self.geometry("500x400")

        c=Control(self)
        c.pack()
        Screen(self).pack()

        self.mainloop()


if __name__=='__main__':
    App()
