from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Lets go Lets get it")



myLabel = Label(root, text="Provinces", fg = ("blue"), bg = ("red"), font = ("arial", 28, "underline"))
def hello():
    labell.config(text = "Ladies and Gentlemen")
myProv = Listbox(root)


myProv.insert(1, "WC ")
myProv.insert(2,"EC")
myProv.insert(3,"NC ")
myProv.insert(4,"NW")

myProv.insert(5,"KZN")
myProv.insert(6,"GN")
myProv.insert(7,"MP")
myProv.insert(8,"LP")
myProv.insert(9,"FS")

labell = Label(root, text = "label")
txtentry = Entry(root)
btn = Button(root, text= "Button", command=(hello))




myLabel.pack()
myProv.pack()
labell.pack()
txtentry.pack()
btn.pack()
root.mainloop()