import numpy as np
from enum import Enum
ccrotate=np.array([[0,-1],[1,0]])
crotate=np.array([[0,1],[-1,0]])
xreflect=np.array([1,0],[0,-1])
yreflect=np.array([-1,0],[0,1])
class Axis(Enum):
	X=1
	Y=2
class Dir(Enum):
	CLOCKWISE=1
	COUNTERCLOCKWISE=2
#reflects vector x over axis axis
def reflect(x,axis):
	if axis==X:
		return np.dot(xreflect,x)
	else:
	    return np.dot(yreflect,x)
#translates vector x by vector h
def translate(x,h):
	return x+h
#dilates vector x by constant c
def dilate(x,c):
	return x*c
#rotates vector x 90 degrees in direction clockwise or counterclockwise
def rotate(x,dir):
	if dir==CLOCKWISE:
		return np.dot(crotate,x)
	else:
		return np.dot(ccrotate,x)
