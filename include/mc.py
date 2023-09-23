#multiple choice class
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
#from . import misc

class multiple_choice():
    def __init__(self,answer_function,choices : list, answer : int,question : str,master : Tk):
        self.master = master
        self.question = question
        self.answer_function = answer_function #Function to update outside of this, there is probably a better was to do this but oh well
        #Frame
        self.frame = Frame(master=self.master)
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.choices = choices
        self.answer = answer
        self.chosen = IntVar(value=4)
        #question
        self.question_label = Label(master=self.frame,text=self.question)
        #choices
        self.m1 = Radiobutton(master=self.frame,text=self.choices[0],variable=self.chosen,value=0)
        self.m2 = Radiobutton(master=self.frame,text=self.choices[1],variable=self.chosen,value=1)
        self.m3 = Radiobutton(master=self.frame,text=self.choices[2],variable=self.chosen,value=2)
        self.m4 = Radiobutton(master=self.frame,text=self.choices[3],variable=self.chosen,value=3)
        #Button to make answer final
        self.final_button = Button(master=self.frame,text="Finish",command=self.onClick)

        #place everything in the right position
        self.frame.grid(row=0,column=0,sticky=N)
        self.question_label.grid(row=0,column=0,columnspan=4,sticky=N)
        self.m1.grid(row=1,column=0,rowspan=1,columnspan=1,padx=2)
        self.m2.grid(row=1,column=1,rowspan=1,columnspan=1,padx=2)
        self.m3.grid(row=1,column=2,rowspan=1,columnspan=1,padx=2)
        self.m4.grid(row=1,column=3,rowspan=1,columnspan=1,padx=2)
        self.final_button.grid(row=2,column=0,columnspan=4,sticky=N) #sticky=N makes it so that it is centered on the columns its on

    def onClick(self):
        if self.chosen.get() == self.answer:
            self.answer_function(True)
            return 1
        else:
            self.answer_function(False)
            return 0



        