from tkinter import *
import tkinter.messagebox as tmsg   
root=Tk()
root.geometry("880x400")
root.title("Radio Button tutorial")
var=StringVar()

def order():
    print("You have ordered "+var.get())
    tmsg.showinfo("Order received","You have ordered "+var.get())
#var.set(1)
Label(root,text="What would you like to have sir?",font=("Times New Roman",14,"bold"),justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa",justify=LEFT).pack()
radio=Radiobutton(root,text="Idli",padx=14,variable=var,value="Idli",justify=LEFT).pack()
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value="Samosa",justify=LEFT).pack()
Button(root,text="Order now",command=order).pack()


root.mainloop()

