
from tkinter import ttk
from tkinter import *
from main.GUI_metoder.kompass import *


class MainView(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.knapp2_clicks=0
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

        self.knapp2 = ttk.Button(self, text="Grafer", padding="2 2 2 2")
        self.knapp2["command"]= self.showGraf
        self.knapp2.grid(row=4, column=1, columnspan=2, sticky=W)

    def showGraf(self):

        self.knapp2_clicks +=1
        if self.knapp2_clicks > 0:
            print(self.knapp2_clicks)
            kompass = Kompass(self)
