from tkinter import *
root = Tk()
root.geometry("300x300")
root.configure(bg="orange")
e = Entry(root, width=50, bg='blue', fg = "white", borderwidth = 5)
e.pack(padx=0, pady=10)
e.insert(0, "Введите ваше имя: ")
def myClick():
    hello = "Привет " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
myButton = Button(root, text = "Нажмите", command=myClick, fg="blue", bg="white")
myButton.pack()
root.mainloop()
