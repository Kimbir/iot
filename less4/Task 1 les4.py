from tkinter import *

root = Tk()
root.geometry("150x80")
root.configure(bg="orange")
mylabel = Label(root, text = "Hello World.", bg='blue', fg = "white", borderwidth = 20)

mylabel.pack()
root.mainloop()