import serial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
import tkinter
import threading




def lesing_arduino():
    # Installering av variabler
    connected = True
    port = 'COM12'
    baud = 9600  # 115200  # 9600

    serieport = serial.Serial(port, baud, timeout=1)

    if serieport.isOpen():
        print(serieport.name, 'er open')
    else:
        serieport.open()

    x = []
    aks_x = []
    aks_y = []
    aks_z = []
    a = []
    b = 0
    runde = 0


    while(1):
        #teikn = serieport.read(1)
        #print(teikn)
        teikn = str(serieport.read(1), encoding='utf-8')  # Les eitt teikn.  #KT La til convert til str
        #print(teikn)
        a.append(teikn)


        if (teikn == "F"):
            k = 1
            l1 = ""
            if(b != 0 ):
                while(a[k] != "Y"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                aks_x.append(int(l1))
                l1 = ""
                k += 1

                while (a[k] != "Z"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                aks_y.append(int(l1))
                l1 = ""
                k += 1

                while (a[k] != "F"):
                    l1 = [l1, a[k]]
                    l1 = "".join(l1)
                    k += 1
                aks_z.append(int(l1))
                l1 = ""
                k += 1

                x.append(runde)
                print("X akse: ",aks_x[runde],"Y akse: ",aks_y[runde],"Z akse: ",aks_z[runde])

                runde += 1
            if(b == 0):
                b = 1
            a = []

lesing = threading.Thread(target=lesing_arduino)
lesing.start()





