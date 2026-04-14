from tkinter import *
root=Tk()
def harry(event):
    print(f"You clicked the button at {event.x}, {event.y}")
root.title("Events in Tkinter")
root.geometry("600x344")
widget=Button(root,text="Click me please")
widget.pack()
widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)
root.mainloop()
