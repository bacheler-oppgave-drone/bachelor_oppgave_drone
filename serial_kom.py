import serial
import queue
import time
import threading

# Installering av variabler
kommando = '0'
brukarkommandoar = queue.Queue()
connected = True
port = 'COM10'
baud = 115200 #115200  # 9600

data = []

serieport = serial.Serial(port, baud, timeout=1)

if serieport.isOpen():
    print(serieport.name, 'er open')
else:
    serieport.open()

def print_data():
    while(1):
        teikn = serieport.read(1)
        #teikn = str(serieport.read(1), encoding='utf-8')  # Les eitt teikn.  #KT La til convert til str
        print(teikn)
serieport.write('k'.encode('utf-8'))
serieport.write('k'.encode('utf-8'))
starting = threading.Thread(target=print_data)
starting.start()

while(1):
    aa=0

    serieport.write('k'.encode('utf-8'))

    #serieport.write('k'.encode('utf-8'))

    #time.sleep(3)

    #serieport.write('s'.encode('utf-8'))

    #time.sleep(3)






