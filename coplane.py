import transform
import numpy as np
import copy
class CoPlane:
	vectors
	def __init__(self):
		vectors=[]
	def insert_shape(self,s):
		for x in s:
			vectors.add(x)
	def insert_vector(self,x):
		vectors.add(x)
	def translate_shape(self,s,h):
		for x in s:
			vectors.add(transform.translate(x,h))
	def reflect_shape(self,s,axis):
		for x in s:
			vectors.add(transform.reflect(s,axis))
	def rotate_shape(self,s,dir):
		for x in s:
			vectors.add(transform.rotate(s,dir))
	def dilate_shape(self,s,c):
		for x in s:
			vectors.add(transform.dilate(s,c))
	def vectors():
		return copy.deepcopy(vectors)

