from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from tkinter import *
from main.GUI_metoder.main_view import *
from main.GUI_metoder.kompass import *
from main.GUI_metoder.last_ned import *
import tkinter
import matplotlib.animation as animation
import threading
from matplotlib.pylab import *

root=Tk()
root.title("Dronnes GUI")

hoved_vindu=MainView(root)

root.mainloop()
