from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from tkinter import *
from main.GUI_metoder.main_view import *
import tkinter
import matplotlib.animation as animation
import threading
from matplotlib.pylab import *

root=Tk()
root.title("Dronnes GUI")
root.geometry("200x50")

hoved_vindu=MainView(root)

root.mainloop()
