from tkinter import *
# root are replace by self
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
        self.title("My GUI class")
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvar=self.var,relief=SUNKEN, anchor='w')
        self.statusbar.pack(side=BOTTOM,fill=Y)

    def click(self):
        print("Click Button")

    def button(self,inptext):
        Button(text=inptext,command=self.click).pack()



if __name__=='__main__':
    window=GUI()
    window.status()
    window.button("Click")
    window.mainloop()