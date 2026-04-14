from tkinter import *
root=Tk()
root.geometry("644x434")
Label(root,text="Welcome to Harry Treavels",font=("comicsansms",19,"bold"),fg="red").grid(row=0,column=3)

name=Label(root,text="Name").grid(row=0,column=1)
phone=Label(root,text="Phone NNumber").grid(row=1,column=1)
gender=Label(root,text="Gender").grid(row=3,column=1)
phone2=Label(root,text="Emergency Contact").grid(row=4,column=1)
paymentmode=Label(root,text="Payment Mode").grid(row=5,column=1)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodvalue=IntVar()



nameentry=Entry(root,textvariable=namevalue).grid(row=0,column=2)
phoneentry=Entry(root,textvariable=phonevalue).grid(row=1,column=2)     
genderentry=Entry(root,textvariable=gendervalue).grid(row=2,column=2)
emergencyentry=Entry(root,textvariable=emergencyvalue).grid(row=3,column=2)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue).grid(row=4,column= 2)
foodvalue=Checkbutton(root,text="Want to prebook your meals?",variable=foodvalue).grid(row=6,column=2)


def getvals():
    print("The name is :",namevalue.get())
    print("The phone number is :",phonevalue.get())
    print("The gender is :",gendervalue.get())
    print("The emergency contact is :",emergencyvalue.get())
    print("The payment mode is :",paymentmodevalue.get())
    print("Prebook meals:", foodvalue.get())

b1=Button(root,text="Submit",command=getvals).grid(row=7,column=3)









root.mainloop()
