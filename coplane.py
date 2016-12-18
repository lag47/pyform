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
			vectors.add()
	def vectors():
		return copy.deepcopy(vectors)

