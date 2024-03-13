import tkinter as tk
from tkinter import ttk

class Control(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.name=tk.StringVar()
        self.label1=tk.Label(self,text="please insert your name:")
        self.entry1=tk.Entry(self,textvariable=self.name)
        self.btn=tk.Button(self,text="Submit")

        self.label1.pack()
        self.entry1.pack()
        self.btn.pack()