import serial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
import tkinter
import threading



# Installering av variabler
connected = True
port = 'COM11'
baud = 57600  # 115200  # 9600 #57600

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
    teikn = serieport.read(1)
    print(teikn)
    # teikn = str(serieport.read(1), encoding='utf-8')
    # print(teikn)
    a.append(teikn)
    # teikn1 = serieport.read(1)
    # print(teikn1)