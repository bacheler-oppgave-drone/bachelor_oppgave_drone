from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from main import serial_kom
import threading
import time

class Kompass(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.plott_kompass()

    def plott_kompass(self):


        time.sleep(1)
        # start_serial_kom = threading.Thread(target=serial_kom.lesing_arduino)
        # start_serial_kom.start()
        self.tid = serial_kom.runde
        self.x = serial_kom.aks_x
        self.y = serial_kom.aks_y
        self.z = serial_kom.aks_z

        f = plt.figure()
        self.graph1 =plt.plot([])


        self.opptater_graph()


    def opptater_graph(self):

        self.graph1.(np.append(self.graph1(), self.x))

        plt.draw()




