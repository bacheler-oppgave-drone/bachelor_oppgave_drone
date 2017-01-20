
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class Kompass(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.plott_kompass()

    def plott_kompass(self):
        self.x = np.linspace(0, 6 * np.pi, 100)
        self.y = np.sin(self.x)

        plt.ion()

        fig = plt.figure()
        ax = fig.add_subplot(111)
        line1, = ax.plot(self.x, self.y, 'r-')

        #self.kompass_plott = Figure(figsize=(5, 5), dpi=70)
        #self.kompass_plott.add_axes()

      #  kompass_graf = self.kompass_plott.add_subplot(111)

        #line1, = kompass_graf.plot(self.x, self.y, 'r-')  # Returns a tuple of line objects, thus the comma

        for phase in np.linspace(0, 10 * np.pi, 500):
            line1.set_ydata(np.sin(self.x + phase))
            fig.canvas.draw()


        self.root = Tk()  # Lager et vindu
        self.root.title("Kompass_plott")  # setter navn på vinduet

        self.tegning = FigureCanvasTkAgg(fig, self.root)
        self.tegning.show()
        self.tegning.get_tk_widget().grid(column=0, row=0)

        self.root.mainloop()
