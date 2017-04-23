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

    def __init__(self, felt1='', felt2='' ):
        self.Felt1 = felt1
        self.Felt2 = felt2
        self.skriving_arduin()

    def skriving_arduin(self):

        connected = True
        port = 'COM19'
        baud = 115200  # 115200  # 9600 #57600

        ser = serial.Serial(port, baud, timeout=1)

        if ser.isOpen():
            print(ser.name, 'er open2')
        else:
            ser.open()

        while 1:
            input1 = str(self.Felt1)
            input2 = str(self.Felt2)

            if input1 == '' or input2=='':
                ser.close()
                exit()
            else:
                time.sleep(0.5)
                # send the character to the device
                # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
                ser.write(('s').encode('utf-8'))
                print("s")
                time.sleep(0.1)
                ser.write((input1).encode('utf-8'))
                print(input1)
                time.sleep(0.1)
                ser.write(('f').encode('utf-8'))
                print("f")
                time.sleep(0.1)
                ser.write(('l').encode('utf-8'))
                print("l")
                time.sleep(0.1)
                ser.write((input2 ).encode('utf-8'))
                print(input2)
                time.sleep(0.1)
                ser.write(('f').encode('utf-8'))
                print("f")
                time.sleep(0.1)
                out = ''
                # let's wait one second before reading output (let's give device time to answer)
                time.sleep(1)
                while ser.inWaiting() > 0:
                    out += ser.read(ser.inWaiting()).decode('utf-8')
                    print(out)
                if out != '':
                    print(">>" + out)
                    if out == 'F' :
                        ser.close()
                        exit()