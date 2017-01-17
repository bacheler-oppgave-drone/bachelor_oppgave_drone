
from tkinter import *

class Kompass(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.plott_kompass()

    def create_mainer(self):