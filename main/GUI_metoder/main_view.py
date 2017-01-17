
from tkinter import *
from tkinter import ttk

class MainView(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_mainer()

    def create_mainer(self):
        self.GPS_koordianter = Label(self, text="Skriv inn GPS koordinater:")
        self.GPS_koordianter.grid(row=0, column=0, columnspan=2, sticky=W)

        self.xKoordiater = Label(self, text="X Koordinater" )
        self.xKoordiater.grid(row=1, column=0, columnspan=2, sticky=W)

        self.Felt1=Entry(self)
        self.Felt1.grid(row=1, column=4, columnspan=2, sticky=W)

        self.yKoordiater = Label(self, text="Y Koordinater")
        self.yKoordiater.grid(row=2, column=0, columnspan=2, sticky=W)

        self.Felt2=Entry(self)
        self.Felt2.grid(row=2, column=4, columnspan=2, sticky=W)

        self.knapp=ttk.Button(self, text= "Last inn", padding="2 2 2 2")
        self.knapp.grid(row=3, column=5, columnspan=2, sticky=W)

