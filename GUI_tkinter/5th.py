from tkinter import *
root=Tk()
root.geometry("644x434")
f1=Frame(root,bg="grey",borderwidth=6,relief=GROOVE)
f1.pack(side=TOP,anchor="nw",fill=Y)
 
def hello():
    print("Hello World Button Clicked")

def name():
    print("Name is Hanshika")

b1= Button(f1,fg="red",text="Print Now",command=hello)
b1.pack(side=TOP,padx=22)

b2= Button(f1,fg="red",text="Tell me your name",command=name)
b2.pack(side=TOP,padx=22)

b3= Button(f1,fg="red",text="Print Now",command=hello)
b3.pack(side=TOP,padx=22)

b4= Button(f1,fg="red",text="Print Now",command=hello)
b4.pack(side=TOP,padx=22)

root.mainloop()