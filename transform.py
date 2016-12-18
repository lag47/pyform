import numpy
from enum import Enum
class Axis(Enum):
	X=1
	Y=2
class Dir(Enum):
	CLOCKWISE=1
	COUNTERCLOCKWISE=2
#reflects vector x over axis axis
def reflect(x,axis):
	return None
#translates vector x by vector h
def translate(x,h):
	return None
#dilates vector x by constant c
def dilate(x,c):
	return None
#rotates vector x 90 degrees in direction clockwise or counterclockwise
def rotate(x,dir):
	return None
