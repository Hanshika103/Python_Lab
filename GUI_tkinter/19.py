from tkinter import *
root=Tk()
root.geometry("655x344")
root.title("icons ")
root.configure(background="grey")
width=root.winfo_screenwidth()
heigth=root.winfo_screenheight()
print(f"{width}x{heigth}")
Button(text="close",command=root.destroy).pack()
root.mainloop()

