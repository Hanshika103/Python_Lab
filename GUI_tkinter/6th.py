from tkinter import *
def getvals():
    print("The username is : ", uservalue.get())
    print("The password is : ", passvalue.get())
root=Tk()
root.geometry("644x434")
a1 = Label(root,text="Username")
a2 = Label(root,text="Password")
a1.grid(column=0)
a2.grid(row=1)



#Variable Classes in Tkinter
#BooleanVar, DoubleVar, IntVar, StringVar

uservalue= StringVar()
passvalue= StringVar()

userentry= Entry(root,textvariable=uservalue)
passentry= Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

b1=Button(root,text="Submit",command=getvals).grid()
root.mainloop()
