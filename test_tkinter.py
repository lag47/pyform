from Tkinter import *
top=Tk()
main_frame=Frame(top)
main_frame.pack()
top_frame=Frame(top)
top_frame.pack(side=TOP)
c=Canvas(main_frame, bg="blue",height=300,width=200)
x=0
def printButton():
	print("button\n")
def drawCircle(x):#probably could get more desired behavior using actual classes
	c.create_polygon(x+10,x+10,x+20,x+20,x+30,x+20,x+10,x+10,fill='red')
	x+=10
b=Button(top_frame,text="Button",command=lambda:drawCircle(x))
b.pack()
c.pack()
top.mainloop()