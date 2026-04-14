from tkinter import *
root=Tk()
root.geometry("600x344")
def upload():
    statusvar.set("Busy..")
    import time 
    time.sleep(2)
    statusvar.set("Ready Now")

    
root.title("Satus Bar")
statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill="both")
Button(root,text="Upload",command=upload).pack()







root.mainloop()
