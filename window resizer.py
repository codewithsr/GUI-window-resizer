from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Window resizer!")
root.geometry("455x452")

def update():
    print("Updating.......")
    root.geometry(f"{width.get()}x{height.get()}")

Label(root, text="Enter the width and height you wish to update your window with", font="lucida 10 italic").grid()

Label(root, text="Width", font="lucida 10 italic").grid(row=3, column=0)
Label(root, text="Height", font="lucida 10 italic").grid(row=4, column=0)

width = StringVar()
height = StringVar()

width = Entry(root)
width.grid(row=3, column=1)

height = Entry(root)
height.grid(row=4, column=1)

Button(root, text='Apply', command=update).grid(row=5, column=0)


root.mainloop()
