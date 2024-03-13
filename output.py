import tkinter as tk
from tkinter import ttk

from setter import Control

class Screen(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        var10=Control(self).name.get()
        t=f"Hello I am {var10}"
        lab2=tk.Label(self,text=t)
        lab2.pack()
