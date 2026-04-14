from tkinter import *
root=Tk()
root.geometry("880x400")
root.title("Scrollbar Tutorial")



#for connnecting scrollbar to text widget
#1. widget(yscrollcommand=scroll.set)
#2. scroll.config(command=widget.yview)


scrollbar=Scrollbar(root)
scrollbar.pack(fill=Y)
listbox=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END,f"item{i}")

listbox.pack(fill="both",padx=22)
scrollbar.config(command=listbox.yview)


text=Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
root.mainloop()