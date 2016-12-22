import coplane
class PlaneCanvas:
	plane
	origin
	scale
	canvas
	def __init__(self,plane,origin,scale,canvas):
		self.plane=plane
		self.origin=origin
		self.scale=scale
		self.canvas=canvas
	def draw_axes(self):
		return None
	def draw_points(self,c):
		vectors=plane.vectors()
		for i in range(0,len(vectors)-1):
			x=scale*vectors[i]+origin
			y=scale*vectors[i+1]+origin
			canvas.create_line(x[0],x[1],y[0],y[1])
	def add_shape(self,s):
		vectors=plane.vectors()
		for x in vectors:
			plane.insert_vector(x)
		draw_points()
	def add_point(self,x):
		plane.insert_vector(x)
		draw_points()
	def reflect_shape(self,s,axis):
		plane.reflect_shape(s,axis)
		draw_points()
	def translate_shape(self,s,h):
		plane.translate_shape(s,h)
		draw_points()
	def rotate_shape(self,s,dir):
		plane.rotate_shape(s,dir)
		draw_points()
	def dilate_shape(self,s,c):
		plane.dilate_shape(s,c)
		draw_points()