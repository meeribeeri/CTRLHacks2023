#multiple choice class
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *

class multiple_choice():
    def __init__(self,choices : list, answer : int,question : str,master : Frame,rowsdown : int):
        self.master = master #window
        self.question = question #The question being asked

        #The frame for all the components
        self.frame = Frame(master=self.master)
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)

        self.choices = choices #All possible choices
        self.answer = answer #The correct choice
        self.chosen = IntVar(value=4) #Which choice was selected
        #question on screen
        self.question_label = Label(master=self.frame,text=self.question)
        #choices (buttons)
        self.m1 = Radiobutton(master=self.frame,text=self.choices[0],variable=self.chosen,value=0)
        self.m2 = Radiobutton(master=self.frame,text=self.choices[1],variable=self.chosen,value=1)
        self.m3 = Radiobutton(master=self.frame,text=self.choices[2],variable=self.chosen,value=2)
        self.m4 = Radiobutton(master=self.frame,text=self.choices[3],variable=self.chosen,value=3)

        #place everything in the right position
        self.frame.grid(row=0+rowsdown,column=0,columnspan=7,sticky=N+E+W)
        self.question_label.grid(row=0,column=0,columnspan=4)
        self.m1.grid(row=1,column=0,rowspan=1,columnspan=1,padx=2)
        self.m2.grid(row=1,column=1,rowspan=1,columnspan=1,padx=2)
        self.m3.grid(row=1,column=2,rowspan=1,columnspan=1,padx=2)
        self.m4.grid(row=1,column=3,rowspan=1,columnspan=1,padx=2)
    
    def delete(self):
        #delete self
        self.frame.destroy()



        