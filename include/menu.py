import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

from include.misc import Question_Box


class TopBar():
    def __init__(self,master : Tk):
        self.master = master
        self.frame = Frame(master=master)
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid(row=0,column=0,columnspan=8,sticky=N)

        self.title = Label(master=self.frame,text="Study Card Duels")
        self.title.grid(row=0,column=1,columnspan=6,sticky=N)


class EndScreen():
    def __init__(self,master : Tk,winner : int):
        self.master = master

        self.frame = Frame(master = master)
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=0,column=0,columnspan=6,rowspan=6,sticky=N)
        self.text = f"Player {winner} wins!"

        self.end_text = Label(master=self.frame,text=self.text)
        self.end_text.grid(row=0,column=0,sticky=N+S)

        self.restart_button = Button(master=self.frame,text="Restart",command=self.restart)
        self.restart_button.grid(row=1,column=0,sticky=N)

    def restart(self):
        for child in self.frame.winfo_children():
            child.destroy()
        self.frame.destroy()
        self.master.quit()

    def delete(self):
        for child in self.frame.winfo_children():
            child.destroy()

        self.frame.destroy()

