from tkinter import *

import clear as clear

root = Tk()
root.title("Калькулятор")
root.geometry("150x330")
root.configure(bg="gray")

def input_into_entry(synbol):
    entry.insert(END, synbol)

def clear():
    entry.delete(0, END)

def count_result():
    text = entry.get()
    result = 0
    if "+" in text:
        splitted_text = text.split("+")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first+second
    if "-" in text:
        splitted_text = text.split("-")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first-second
    if "/" in text:
        splitted_text = text.split("/")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first/second
    if "*" in text:
        splitted_text = text.split("*")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first*second
    clear()
    entry.insert(0, result)


entry = Entry(root, width=23, bg='white', fg = "black", borderwidth = 5)
entry.place(x=0, y=0)

b1= Button(root, bg="white", fg = "black", text="1", command=lambda: input_into_entry(1))
b1.place(x=0, y=30, width=50, height=50)

b2= Button(root, bg="white", fg = "black", text="2", command=lambda: input_into_entry(2))
b2.place(x=50, y=30, width=50, height=50)

b3= Button(root, bg="white", fg = "black", text="3", command=lambda: input_into_entry(3))
b3.place(x=100, y=30, width=50, height=50)

b4= Button(root, bg="white", fg = "black", text="4", command=lambda: input_into_entry(4))
b4.place(x=0, y=80, width=50, height=50)

b5= Button(root, bg="white", fg = "black", text="5", command=lambda: input_into_entry(5))
b5.place(x=50, y=80, width=50, height=50)

b6= Button(root, bg="white", fg = "black", text="6", command=lambda: input_into_entry(6))
b6.place(x=100, y=80, width=50, height=50)

b7= Button(root, bg="white", fg = "black", text="7", command=lambda: input_into_entry(7))
b7.place(x=0, y=130, width=50, height=50)

b8= Button(root, bg="white", fg = "black", text="8", command=lambda: input_into_entry(8))
b8.place(x=50, y=130, width=50, height=50)

b9= Button(root, bg="white", fg = "black", text="9", command=lambda: input_into_entry(9))
b9.place(x=100, y=130, width=50, height=50)

b0= Button(root, bg="white", fg = "black", text="0", command=lambda: input_into_entry(0))
b0.place(x=0, y=180, width=50, height=50)

bdel= Button(root, bg="white", fg = "black", text="Очистить", command = clear)
bdel.place(x=50, y=180, width=100, height=50)

bp= Button(root, bg="white", fg = "black", text="+", command=lambda: input_into_entry("+"))
bp.place(x=0, y=230, width=50, height=50)

bm= Button(root, bg="white", fg = "black", text="-", command=lambda: input_into_entry("-"))
bm.place(x=0, y=280, width=50, height=50)

br= Button(root, bg="white", fg = "black", text="=", command=count_result)
br.place(x=50, y=230, width=100, height=50)

by= Button(root, bg="white", fg = "black", text="*", command=lambda: input_into_entry("*"))
by.place(x=50, y=280, width=50, height=50)

bd= Button(root, bg="white", fg = "black", text="/", command=lambda: input_into_entry("/"))
bd.place(x=100, y=280, width=50, height=50)

root.mainloop()