from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("880x400")
root.title("Slider tutorial")
def getdollars():
    tmsg.showinfo("Amount in dollars",f"Amount in dollars is : {myslider1.get()*88.2}")
Label(text="Volume").pack()
myslider=Scale(root,from_=0,to=100)
myslider.pack()

myslider1=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=25)
myslider1.pack()

Button(root,text="Get dollars!",command=getdollars).pack()


root.mainloop()
