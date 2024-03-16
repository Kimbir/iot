from tkinter import *
root = Tk()
root.geometry("300x300")
root.configure(bg="orange")
def myClick():
    myLabel = Label(root, text="Нажата кнопка!")
    myLabel.pack()
myButton = Button(root, text = "Нажмите", command=myClick, fg="blue", bg="white")
myButton.pack()
root.mainloop()