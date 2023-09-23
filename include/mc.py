#multiple choice class
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
#from . import misc

class multiple_choice():
    def __init__(self,choices : list, answer : int,question : str,master : Tk):
        self.master = master
        self.question = question
        self.frame = Frame(master=self.master)
        self.frame.grid(column=5,row=5)
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.choices = choices
        self.answer = answer
        self.question_label = Label(master=self.frame,text=self.question)
        self.question_label.grid(column=5,row=5)


        