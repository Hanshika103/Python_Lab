from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("644x434")
root.title("CodeWithHarry GUI") 

def myfunc():
    print("Hello you clicked me")

def help():
    print("I will help you")
    tmsg.showinfo("Hello, Help","I will help you")

def rate():
    print("Rate us")
    value=tmsg.askquestion("Rate us","Please rate us 5 stars")
    if value=="yes":
        tmsg.showinfo("Thanks","Thanks for rating us 5 stars")
    else:
        tmsg.showinfo("No Problem","Thanks for your response")

def divya():
    ans=tmsg.askretrycancel("Divya","You are Divya?")
    if ans:
        print("You are Divya")
    else:
        print("You are not Divya")

filemenu=Menu(root)
m1=Menu(filemenu,tearoff=0)
m1.add_command(label="New Project",command=help)
m1.add_command(label="New",command=myfunc)
m1.add_separator()
m1.add_command(label="Save",command=help)
m1.add_command(label="Save As",command=rate)
filemenu.add_cascade(label="File", menu=m1)
root.config(menu=filemenu)

m2=Menu(filemenu,tearoff=0)
m2.add_command(label="Cut",command=divya)
m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Paste",command=rate)
filemenu.add_cascade(label="Edit", menu=m2)
root.config(menu=filemenu)



m3=Menu(filemenu,tearoff=0)
m3.add_command(label="Find",command=myfunc)    
m3.add_command(label="Replace",command=myfunc)
filemenu.add_cascade(label="Find", menu=m3)
root.config(menu=filemenu)

root.mainloop()
