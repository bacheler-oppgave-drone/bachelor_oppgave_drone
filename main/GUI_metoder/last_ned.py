from tkinter import *
import serial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from main import serial_kom
import threading
import time
import matplotlib.animation as anim
from mpl_toolkits.mplot3d import Axes3D
from main import serial_kom

class last_ned:

    def __init__(self, felt1=Entry, felt2=Entry ):
        self.Felt1 = felt1
        self.Felt2 = felt2
        self.skriving_arduin()

    def skriving_arduin(self):

        connected = True
        port = 'COM19'
        baud = 115200  # 115200  # 9600 #57600

        ser = serial.Serial(port, baud, timeout=1)

        if ser.isOpen():
            print(ser.name, 'er open')
        else:
            ser.open()

        while 1:
            input1 = str(self.Felt1)
            input2 = str(self.Felt2)

            if input1 == '' or input2=='':
                ser.close()
                exit()
            else:
                # send the character to the device
                # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
                ser.write((input1 + '\r\n').encode('utf-8'))
                ser.write((input2 + '\r\n').encode('utf-8'))

                out = ''
                # let's wait one second before reading output (let's give device time to answer)
                time.sleep(1)
                while ser.inWaiting() > 0:
                    out += ser.read(1).decode('utf-8')
                    print("tekst")


                if out != '':
                    print(">>" + out)
                    if out == 'fine' :
                        ser.close()
                        exit()