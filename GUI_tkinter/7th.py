from tkinter import *
root=Tk()
root.geometry("644x434")
#a1=Label(root,text="Enter Name for Dance Class",bg="Pink",fg="black",font=("Arial",15,"bold"),padx=10,pady=10,relief=RAISED,borderwidth=5)
#a1.pack(pady=20)
l=Label(root,text="Enter Name: ")
l.pack()
uservalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
userentry.pack()
b1=Button(root,text="Submit",command=lambda:print("Name entered is :",uservalue.get()))
b1.pack(pady=10)

root.mainloop()
