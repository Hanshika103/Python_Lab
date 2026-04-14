from tkinter import *
root=Tk()

canvas_width=880
canvas_height=400


root.geometry(f"{canvas_width}x{canvas_height}")
can_weiget=Canvas(root,width=canvas_width,height=canvas_height  )
can_weiget.pack()
#the lines goes from the point x1,y1 to x2,y2 ek line create hoti hai wo ki x and y axis se upper and lower hoti hai
can_weiget.create_line(0,0,800,200,fill="red")
can_weiget.create_line(0,200,800,0,fill="red")
root.title("My first GUI program")
# to create a rectangle specifically create this other parameters
can_weiget.create_rectangle(3,5,700,300,fill="blue")
#to create oval in a rectangle only
can_weiget.create_oval(20,20,300,200,fill="yellow")
can_weiget.create_oval(400,100,600,300,fill="green")

#create text feature in GUI

can_weiget.create_text(200,200,text="Welcome to Harry Travels",font=("comicsansms",24,"bold"),fill="white")
root.mainloop()