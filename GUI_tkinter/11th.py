from tkinter import *
root=Tk()
root.geometry("880x400")
root.title("Pycharm")
def myfunc():
    print("You clicked the menu item")

# use this to create to run dropdown menu
mymenu= Menu(root)
mymenu.add_command(label="File",command=myfunc)
mymenu.add_command(label="Edit",command=quit)


root.config(menu=mymenu)

mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save As",command=myfunc)
m1.add_separator()
m1.add_command(label="Save All",command=myfunc)
mainmenu.add_cascade(label="File",menu=m1)
root.config(menu=mainmenu)


mainmenu=Menu(root)
m2=Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="File",menu=m1)

m2.add_command(label="print",command=myfunc)
m2.add_command(label="use",command=myfunc)
m2.add_command(label="correct",command=myfunc)
mainmenu.add_cascade(label="File",menu=m2)
root.config(menu=mainmenu)




root.mainloop()
