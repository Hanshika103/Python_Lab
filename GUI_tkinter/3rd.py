from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("My First GUI Application")
#Important Labels Options
'''text - adds the Text
bd - background
fig - foreground
font - sets the font, font=("Times New Roman",15,"bold")
padx - x padding
pady - y padding
relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE'''
title_label = Label(text="Welcome on my application",bg="red",fg="white",padx=23,pady=36,font=("Times New Roman",15,"bold"),borderwidth=3,relief=SUNKEN)
title_label.pack(side="top", anchor="ne",fill="x")

#Important Pack Options
''' anchor - nw, ne, sw, se
side - top, bottom, left, right
fill - x, y, both'''
root.mainloop()