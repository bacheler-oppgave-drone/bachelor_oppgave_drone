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

        f = plt.figure()
        graph1 = f.add_subplot(221)
        graph2 = f.add_subplot(222)
        graph3 = f.add_subplot(223)
        graph4 = f.add_subplot(224)
        #kompass = f.add_subplot(2,1,2,projection='3d')

        self.tid = serial_kom.runde
        self.x = serial_kom.aks_x
        self.y = serial_kom.aks_y
        self.z = serial_kom.aks_z
        self.kp_x = serial_kom.kompass_x
        self.kp_y = serial_kom.kompass_y
        self.kp_z = serial_kom.kompass_z

        def up(i):
            graph1.clear()
            graph1.plot(self.x)
            graph2.clear()
            graph2.plot(self.y)
            graph3.clear()
            graph3.plot(self.z)
            graph4.clear()
            graph4.plot(self.kp_x)


        a = anim.FuncAnimation(f, up, repeat=False,blit=False,interval=1000)
        plt.show()












