
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

        line1.set_ydata(np.sin(self.x))

        fig.canvas.draw()

