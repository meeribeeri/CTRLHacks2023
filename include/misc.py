import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

class Question_Text():
    def __init__(self,question : str, frame : Frame):
        self.question = question
        self.label = Label(frame,question,anchor="center")

class Question_Box():
    def __init__(self,master : Tk):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=1,column=1,columnspan=6,rowspan=7,sticky=N)

        self.title = Label(master=self.frame,text="Answer All Questions")
        self.title.grid(row=0,column=0,columnspan=6,sticky=N)

        self.final_answer = Button(master=self.frame,text="Finish")
        self.final_answer.grid(row=7,column=0,columnspan=6,sticky=N)