


from tkinter import *
from PIL import Image, ImageTk 

hanshika_root = Tk()
hanshika_root.geometry("400x400")

#photo = PhotoImage(file="11.jpg") 
image = Image.open("11.jpg")  # 👈 local file path
photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)
varun_label.pack()

hanshika_root.mainloop()
