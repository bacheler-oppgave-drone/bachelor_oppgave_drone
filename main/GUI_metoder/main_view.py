import time
from tkinter import ttk
from tkinter import *
from main.GUI_metoder.kompass import *
from main.GUI_metoder.last_ned import *
from main.serial_kom import *


class MainView(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        serial_kom.lasting=0
        self.grid()
        self.knapp_clicks = 0
        self.knapp2_clicks = 0
        self.knapp3_clicks = 0
        self.knapp4_clicks = 0
        self.knapp5_clicks = 0
        self.knapp6_clicks = 0
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

        self.hoyde = Label(self, text="Høyde")
        self.hoyde.grid(row=3, column=0, columnspan=2, sticky=W)

        self.Felt3=Entry(self)
        self.Felt3.grid(row=3, column=4, columnspan=2, sticky=W)

        self.knapp=ttk.Button(self, text= "Last inn", padding="2 2 2 2")
        self.knapp["command"] = self.last_ned
        self.knapp.grid(row=4, column=5, columnspan=2, sticky=W)

        #---------------------------------------------------------------------------------------------------------------

        self.Kontinuerlig_ploting = Label(self, text="Kontinuerlig plotting:" ,font=("Helvetica", 11))
        self.Kontinuerlig_ploting.grid(row=5, column=0, columnspan=2, sticky=S)

        self.knapp2 = ttk.Button(self, text="Pådrag til motorene", padding="8 1 8 1")
        self.knapp2["command"]= self.showGraf
        self.knapp2.grid(row=6, column=1, columnspan=2, sticky=W)

        self.knapp3 = ttk.Button(self, text="Gyroskop", padding="27 1 27 1")
        self.knapp3["command"]= self.PID_grafer
        self.knapp3.grid(row=7, column=1, columnspan=2, sticky=W)

        self.knapp4 = ttk.Button(self, text="Avvik", padding="27 1 27 1")
        self.knapp4["command"]= self.avvik_grafer
        self.knapp4.grid(row=8, column=1, columnspan=2, sticky=W)

        self.knapp5 = ttk.Button(self, text="PID", padding="27 1 27 1")
        self.knapp5["command"]= self.vinkler_grafer
        self.knapp5.grid(row=9, column=1, columnspan=2, sticky=W)

        #---------------------------------------------------------------------------------------------------------------

        self.Kontinuerlig_ploting = Label(self, text="Data samling:", font=("Helvetica", 11))
        self.Kontinuerlig_ploting.grid(row=10, column=0, columnspan=2, sticky=S)

        self.knapp6 = ttk.Button(self, text="Sortering til matlab", padding="10 1 10 1")
        self.knapp6["command"]= self.filtrering_matlab
        self.knapp6.grid(row=11, column=1, columnspan=1, sticky=W)


    def last_ned(self):
        self.knapp_clicks +=1
        if self.knapp_clicks > 0:
            serial_kom.lasting=1
            time.sleep(1)
            late = last_ned(self.Felt1.get(), self.Felt2.get(), self.Felt3.get())

    def showGraf(self):

        self.knapp2_clicks +=1
        if self.knapp2_clicks > 0:
            kompass = Kompass(self)

    def PID_grafer(self):

        self.knapp3_clicks +=1
        if self.knapp3_clicks > 0:
            pid_frame = PID_frame(self)


    def avvik_grafer(self):
        self.knapp4_clicks += 1
        if self.knapp4_clicks > 0:
            avvik_frame = Avvik_frame(self)

    def vinkler_grafer(self):
        self.knapp5_clicks += 1
        if self.knapp5_clicks > 0:
            vinkler_frame = Vinkler_frame(self)

    def filtrering_matlab(self):
        self.knapp6_clicks += 1
        if self.knapp6_clicks > 0:
            matlab_frame = Vinkler_frame(self)