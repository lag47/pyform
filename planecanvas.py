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
	def draw(c):
		vectors=plane.vectors()
		for i in range(0,len(vectors)-1):
			y=x
			canvas.create_line(y[0],y[1])
		return None