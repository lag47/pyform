import shapeloader
import planecanvas
from Tkinter import *
import numpy as np
top=Tk()
button_frame=Frame(top)
button_frame.pack(side=TOP)
main_frame=Frame(top)
c=Canvas(main_frame, bg="white",height=300,width=200)
pc=PlaneCanvas(CoPlane(),np.a[])
