import serial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
import tkinter
import threading
from main.GUI_metoder.main_view import *

global aks_x
global aks_y
global aks_z
global kompass_x
global kompass_y
global kompass_z
global runde

def lesing_arduino():
    # Installering av variabler
    connected = True
    port = 'COM19'
    baud = 115200  # 115200  # 9600 #57600

    serieport = serial.Serial(port, baud, timeout=1)

    if serieport.isOpen():
        print(serieport.name, 'er open')
    else:
        serieport.open()

    global x
    global a
    global motor1
    global motor2
    global motor3
    global motor4
    global e_theta
    global e_phi
    global e_sai
    global u_theta
    global u_phi
    global u_sai
    global vin_theta
    global vin_phi
    global vin_sai
    global runde
    global lasting

    lasting=0
    x = []
    a = []
    motor1 = []
    motor2 = []
    motor3 = []
    motor4 = []
    e_theta = []
    e_phi = []
    e_sai = []
    u_theta = []
    u_phi = []
    u_sai = []
    vin_theta = []
    vin_phi = []
    vin_sai = []
    b = 0
    runde = 0
    start_sjekk = 0

    while(1):
        teikn = str(serieport.read(1), encoding='utf-8')
        print(teikn)
        a.append(teikn)

        if (teikn == "F"):
            k = 1
            l1 = ""
            if(b != 0 ):
                #----------------------akselaerasjon
                while(a[k] != "Y"):
                    if(a[k] != "X"):
                        l1 = [l1, a[k]]
                        l1 = "".join(l1)
                        k += 1
                motor1.append(float(l1))
                l1 = ""
                k += 1

                while (a[k] != "Z"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                motor2.append(float(l1))
                l1 = ""
                k += 1

                while (a[k] != "A"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                motor3.append((float(l1)))
                l1 = ""
                k += 1

                while (a[k] != "B"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                motor4.append(float(l1))
                l1 = ""
                k += 1
                # ------------------------------------------------------
                while (a[k] != "C"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                e_theta.append(float(l1))
                l1 = ""
                k += 1

                while (a[k] != "D"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                e_phi.append(float(l1))
                l1 = ""
                k += 1

                while (a[k] != "E"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                e_sai.append(float(l1))
                l1 = ""
                k += 1
                # ------------------------------------------------------
                while (a[k] != "G"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                u_theta.append(float(l1))
                l1 = ""
                k += 1


                while (a[k] != "H"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                u_phi.append(float(l1))
                l1 = ""
                k += 1



                while (a[k] != "I"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                u_sai.append(float(l1))
                l1 = ""
                k += 1

                # ------------------------------------------------------
                while (a[k] != "J"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                vin_theta.append(float(l1))
                l1 = ""
                k += 1

                while (a[k] != "L"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                vin_phi.append(float(l1))
                l1 = ""
                k += 1

                while (a[k] != "F"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                vin_sai.append(float(l1))
                l1 = ""
                k += 1


                x.append(runde)
                runde += 0.05
            if(b == 0):
                b = 1
            a = []
        if lasting==1:
            return

lesing = threading.Thread(target=lesing_arduino)
lesing.start()



