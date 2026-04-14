from tkinter import *
root=Tk()

root.geometry("880x400")
root.title("List Box Tutorial")
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0
Label(root,text="Select your favorite programming language:",font=("Helvetica",16,"bold")).pack(pady=10)

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"Python")
Button(root,text="add iteam",command=add).pack()






root.mainloop()