import serial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
import tkinter
import threading


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
    port = 'COM4'
    baud = 9600  # 115200  # 9600

    serieport = serial.Serial(port, baud, timeout=1)

    if serieport.isOpen():
        print(serieport.name, 'er open')
    else:
        serieport.open()

    global aks_x
    global aks_y
    global aks_z
    global kompass_x
    global kompass_y
    global kompass_z
    global runde

    x = []
    aks_x = []
    aks_y = []
    aks_z = []
    kompass_x = []
    kompass_y = []
    kompass_z = []
    a = []
    b = 0
    runde = 0
    start_sjekk = 0

    while(start_sjekk == 0):
        teikn = str(serieport.read(1), encoding='utf-8')
        if(teikn == "F"):
            start_sjekk = 1
    while(1):
        #teikn = serieport.read(1)
        #print(teikn)
        teikn = str(serieport.read(1), encoding='utf-8')
        #print(teikn)
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
                aks_x.append(float(l1))
                l1 = ""
                k += 1

                while (a[k] != "Z"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                aks_y.append(float(l1))
                l1 = ""
                k += 1

                while (a[k] != "A"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                aks_z.append((float(l1)))
                l1 = ""
                k += 1

                # ----------------------gyroskop
                while (a[k] != "B"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                kompass_x.append(float(l1))
                l1 = ""
                k += 1

                while (a[k] != "C"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                kompass_y.append(float(l1))
                l1 = ""
                k += 1

                while (a[k] != "F"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                kompass_z.append(float(l1))
                l1 = ""
                k += 1


                print("X akse: ", aks_x[runde], "Y akse: ", aks_y[runde], "Z akse: ", aks_z[runde])
                #print("X kompass: ", kompass_x[runde], "Y kompass: ", kompass_y[runde], "Z kompass: ", kompass_z[runde])

                


                x.append(runde)
                runde += 1
            if(b == 0):
                b = 1
            a = []

lesing = threading.Thread(target=lesing_arduino)
lesing.start()





