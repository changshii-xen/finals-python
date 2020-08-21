from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Exercise 1")

def add():
    x = float(Number1.get())
    y = float(Number2.get())
    answer = x + y
    result.set(answer)

def sub():
    x = float(Number1.get())
    y = float(Number2.get())
    answer = x - y
    result.set(answer)

def mult():
    x = float(Number1.get())
    y = float(Number2.get())
    answer = x * y
    result.set(answer)

def div():
    x = float(Number1.get())
    y = float(Number2.get())
    answer = x / y
    result.set(answer)

def clear():
    Number1.set(" ")
    Number2.set(" ")
    result.set(" ")
def close():
    root.destroy()


frame1 = Frame(root)

frame2 = Frame(frame1)
frame2.grid(row=1, column=0)
Number1= StringVar()
Number2=StringVar()
result=StringVar()

num1 = Label(frame2, text = "Please enter first number:")
num1.grid(row=1, column=1)
txtNum1Entry = Entry(frame2, textvariable=Number1)
txtNum1Entry.grid(row=1, column=2)
num2 = Label(frame2, text="Please enter second  number:")
num2.grid(row=2, column=1)
txtNum2Entry = Entry(frame2, textvariable=Number2)
txtNum2Entry.grid(row=2, column=2)
answerLabel = Label(frame2, text="Your Answer:")
answerLabel.grid(row=3, column=1)
answerShow = Label(frame2, text="Answer", textvariable=result)
answerShow.grid(row=3, column=2)
frame3 = Frame(frame1)
frame3.grid(row=2, column=0)

addBtn = Button(frame3, text="Add", command=add)
addBtn.grid(row=0, column=1)
subBtn = Button(frame3, text="Subtract", command=sub)
subBtn.grid(row=0, column=2)
multBtn = Button(frame3, text="Multiply", command=mult)
multBtn.grid(row=0, column=3)
divBtn = Button(frame3, text="Divide", command=div)
divBtn.grid(row=0, column=4)
clearBtn = Button(frame3, text="Clear", command=clear)
clearBtn.grid(row=0, column=5)
exitBtn = Button(frame3, text="Exit", command=close)
exitBtn.grid(row=0, column=6)



frame1.pack()
root.mainloop()