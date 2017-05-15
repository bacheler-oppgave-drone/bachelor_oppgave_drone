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

        f = plt.figure(figsize=(12,12))
        f.suptitle('Pådrag på motorene', fontsize=14, fontweight='bold')
        f.subplots_adjust(wspace=0.3)

        graph1 = f.add_subplot(221)
        graph2 = f.add_subplot(222)
        graph3 = f.add_subplot(223)
        graph4 = f.add_subplot(224)
        #kompass = f.add_subplot(2,1,2,projection='3d')

        self.tid = serial_kom.runde
        self.x = serial_kom.motor1
        self.y = serial_kom.motor2
        self.z = serial_kom.motor3
        self.kp_x = serial_kom.motor4


        def up(i):
            graph1.clear()
            graph1.plot(self.x)
            graph2.clear()
            graph2.plot(self.y)
            graph3.clear()
            graph3.plot(self.z)
            graph4.clear()
            graph4.plot(self.kp_x)

            graph1.set_title("Motor1")
            graph2.set_title("Motor2")
            graph3.set_title("Motor3")
            graph4.set_title("Motor4")

            graph1.set_xlabel('Tid i sekund')
            graph1.set_ylabel('PWM-signal i mikrosekund')
            graph2.set_xlabel('Tid i sekund')
            graph2.set_ylabel('PWM-signal i mikrosekund')
            graph3.set_xlabel('Tid i sekund')
            graph3.set_ylabel('PWM-signal i mikrosekund')
            graph4.set_xlabel('Tid i sekund')
            graph4.set_ylabel('PWM-signal i mikrosekund')


        a = anim.FuncAnimation(f, up, repeat=False,blit=False,interval=1000)
        plt.show()



class PID_frame(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.plott_PID()

    def plott_PID(self):

        PID = plt.figure(figsize=(13,5))

        PID.suptitle('Vinkelen til dronen', fontsize=14, fontweight='bold')
        PID.subplots_adjust(wspace=0.3)

        graph1 = PID.add_subplot(131)

        graph2 = PID.add_subplot(132)
        graph3 = PID.add_subplot(133)




        self.x = serial_kom.e_theta
        self.y = serial_kom.e_phi
        self.z = serial_kom.e_sai

        def up(i):
            graph1.clear()
            graph1.plot(self.x)
            graph2.clear()
            graph2.plot(self.y)
            graph3.clear()
            graph3.plot(self.z)

            graph1.set_title("theta")
            graph2.set_title("phi")
            graph3.set_title("sai")

            graph1.set_xlabel('Tid i sekund')
            graph1.set_ylabel('Grader')
            graph2.set_xlabel('Tid i sekund')
            graph2.set_ylabel('Grader')
            graph3.set_xlabel('Tid i sekund')
            graph3.set_ylabel('Grader')




        a2 = anim.FuncAnimation(PID, up, repeat=False,blit=False,interval=1000)
        plt.show()

class Avvik_frame(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.plott_Avvik()

    def plott_Avvik(self):

        PID = plt.figure(figsize=(13,5))
        PID.suptitle('Avviket', fontsize=14, fontweight='bold')
        PID.subplots_adjust(wspace=0.3)

        graph1 = PID.add_subplot(131)

        graph2 = PID.add_subplot(132)

        graph3 = PID.add_subplot(133)




        self.x = serial_kom.u_theta
        self.y = serial_kom.u_phi
        self.z = serial_kom.u_sai


        def up(i):
            graph1.clear()
            graph1.plot(self.x)
            graph2.clear()
            graph2.plot(self.y)
            graph3.clear()
            graph3.plot(self.z)



            graph1.set_title("Avvik theta ")
            graph2.set_title("Avvik phi")
            graph3.set_title("Avvik sai ")

            graph1.set_xlabel('Tid i sekund')
            graph1.set_ylabel('Grader')
            graph2.set_xlabel('Tid i sekund')
            graph2.set_ylabel('Grader')
            graph3.set_xlabel('Tid i sekund')
            graph3.set_ylabel('Grader')




        a3 = anim.FuncAnimation(PID, up, repeat=False,blit=False,interval=1000)
        plt.show()



class Vinkler_frame(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.plott_Avvik()

    def plott_Avvik(self):

        PID = plt.figure(figsize=(13,5))
        PID.suptitle('PID-leddene til regulatoren', fontsize=14, fontweight='bold')
        PID.subplots_adjust(wspace=0.3)
        graph1 = PID.add_subplot(131)

        graph2 = PID.add_subplot(132)

        graph3 = PID.add_subplot(133)



        self.x = serial_kom.vin_theta
        self.y = serial_kom.vin_phi
        self.z = serial_kom.vin_sai

        def up(i):
            graph1.clear()
            graph1.plot(self.x)
            graph2.clear()
            graph2.plot(self.y)
            graph3.clear()
            graph3.plot(self.z)



            graph1.set_title("P-leddet")
            graph2.set_title("I-leddet")
            graph3.set_title("D-leddet")

            graph1.set_xlabel('Tid i sekund')
            graph2.set_xlabel('Tid i sekund')
            graph3.set_xlabel('Tid i sekund')


        a4 = anim.FuncAnimation(PID, up, repeat=False,blit=False,interval=1000)
        plt.show()








