from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from main import serial_kom
import threading
import time
import matplotlib.animation as anim
from mpl_toolkits.mplot3d import Axes3D


class Kompass(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.plott_kompass()

    def plott_kompass(self):

        time.sleep(1)

        f = plt.figure()
        graph1 =f.add_subplot(231)
        graph2 = f.add_subplot(232)
        graph3 = f.add_subplot(233)
        kompass = f.add_subplot(2,3,4,projection='3d')

        self.tid = serial_kom.runde
        self.x = serial_kom.aks_x
        self.y = serial_kom.aks_y
        self.z = serial_kom.aks_z

        def up(i):
            graph1.clear()
            graph1.plot(self.x)
            graph2.clear()
            graph2.plot(self.y)
            graph3.clear()
            graph3.plot(self.z)

        a = anim.FuncAnimation(f, up, repeat=False,blit=False,interval=1000)
        plt.show()












