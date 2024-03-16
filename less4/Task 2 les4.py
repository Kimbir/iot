from tkinter import *

root = Tk()
root.geometry("300x300")
root.configure(bg="orange")
mylabel1 = Label(root, text = "Hello World.", bg='blue', fg = "white", borderwidth = 10)
mylabel1.grid(row=0, column=0)
mylabel2 = Label(root, text = "                              ", bg='blue', fg = "white", borderwidth = 10)
mylabel2.grid(row=0, column=5)
mylabel3 = Label(root, text = "                   ", bg='blue', fg = "white", borderwidth = 10)
mylabel3.grid(row=1, column=0)
mylabel4 = Label(root, text = "My Name Is Vladimir", bg='blue', fg = "white", borderwidth = 10)
mylabel4.grid(row=1, column=5)

root.mainloop()