from tkinter import *
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ "-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

        root.title(os.path.basename(file)+ " - Notepad")


def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt'),defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")]
        if file =="":
            file=None  
        else:
            #Save as a new file
            f=open(file, "w")
            f.write(TextArea.get(1.0,END))
            f.close()

def quitApp():
    root.destroy()  # closes the app

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad","Notepad by ")


if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    # root.wm_iconbitmap("1.ico")
    root.geometry("644x788")

    # Add text area
    TextArea = Text(root, font="lucida 13")
    TextArea.pack(fill=BOTH, expand=True)
    file = None

    # Create MenuBar
    MenuBar = Menu(root)

    # ========== File Menu ==========
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    # ========== Edit Menu ==========
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # ========== Help Menu ==========
    HelpMenu = Menu(MenuBar, tearoff=0)   # <-- Fixed typo (was 'teraoff')
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Configure the menu

    root.config(menu=MenuBar)

    #Adding scrollbar using rules from tkimter lecture
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    # Start the GUI loop
    root.mainloop()
