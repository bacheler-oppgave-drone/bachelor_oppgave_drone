
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Kompass(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.plott_kompass()

    def plott_kompass(self):
        self.figur_test = Figure(figsize=(5, 5), dpi=70)
        self.figur_test.add_axes()
        avstand_graf = self.figur_test.add_subplot(111)

        self.root = Tk()  # Lager et vindu
        self.root.title("Gruppe 2 Analyse av data")  # setter navn på vinduet

        self.tegning = FigureCanvasTkAgg(self.figur_test, self.root)
        self.tegning.show()
        self.tegning.get_tk_widget().grid(column=0, row=0)

        self.root.mainloop()
