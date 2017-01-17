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
    port = 'COM13'
    baud = 9600  # 115200  # 9600

    serieport = serial.Serial(port, baud, timeout=1)

    if serieport.isOpen():
        print(serieport.name, 'er open')
    else:
        serieport.open()

    x = []
    data_pin4 = []
    data_pin5 = []
    telling = 0
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

            l1 = [a[b - 6], a[b - 5], a[b - 4]]
            pin4 = ''.join(l1)

            l1 = [a[b-3],a[b-2],a[b-1]]
            pin5 = ''.join(l1)

            data_pin4.append(pin4)
            data_pin5.append(pin5)
            x.append(runde)
            print("Pine4: ",data_pin4[runde]," Pine5: ",data_pin5[runde])
            runde += 1

        b += 1


lesing = threading.Thread(target=lesing_arduino)
lesing.start()

figur_test = Figure(figsize=(5, 5), dpi=70)
figur_test.add_axes()
avstand_graf = figur_test.add_subplot(111)

root = Tk()                           # Lager et vindu
root.title("Gruppe 2 Analyse av data")# setter navn på vinduet

Figure = FigureCanvasTkAgg(figur_test,root)
Figure.show()
Figure.get_tk_widget().grid(column=0, row=0)

root.mainloop()









