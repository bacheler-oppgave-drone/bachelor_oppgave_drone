
from tkinter import *


class MainView(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_mainer()

    def create_mainer(self):
        self.Felt1=Entry()
        self.Felt1.grid()

        self.Felt2=Entry()
        self.Felt1.grid()

        self.knapp=Button(self, text= "Tekst")
        self.knapp.grid()

