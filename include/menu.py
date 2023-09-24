import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *


class TopBar():
    def __init__(self,master : Tk):
        self.master = master
        self.frame = Frame(master=master)
        self.frame['borderwidth'] = 2
        self.frame['relief'] = 'sunken'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid(row=0,column=0,columnspan=8,sticky=N)

        self.title = Label(master=self.frame,text="Title Goes Here Bois!")
        self.title.grid(row=0,column=1,columnspan=6,sticky=N)

        self.menu_button = Button(master=self.frame,text="Menu",command=self.openMenu)
        self.menu_button.grid(row=0,column=0,sticky=N)

    def openMenu(self):
        pass
