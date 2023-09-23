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
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.choices = choices
        self.answer = answer
        #question
        self.question_label = Label(master=self.frame,text=self.question)
        #choices
        self.m1 = Radiobutton(master=self.frame,text=self.choices[0])
        self.m2 = Radiobutton(master=self.frame,text=self.choices[1])
        self.m3 = Radiobutton(master=self.frame,text=self.choices[2])
        self.m4 = Radiobutton(master=self.frame,text=self.choices[3])

        #pack everything
        self.frame.pack()
        self.question_label.pack()
        self.m1.pack()
        self.m2.pack()
        self.m3.pack()
        self.m4.pack()



        