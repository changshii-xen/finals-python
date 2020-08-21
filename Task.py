from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("LIFECHOICES PROGRESS CLACULATOR")

frame1 = Frame(root)

frame2 = Frame(frame1)
frame2.grid(row=1, column=0)

studInfo = Label(frame2, text="Student Information")
studInfo.grid(row=0, column=1)
studentNo = Label(frame2, text="Student No:")
studentNo.grid(row=1, column=1)
txtStudNoEntry = Entry(frame2)
txtStudNoEntry.grid(row=1, column=2)
name = Label(frame2, text="          Name:")
name.grid(row=2, column=1)
txtNameEntry = Entry(frame2)
txtNameEntry.grid(row=2, column=2)


frame3 = Frame(frame1)
frame3.grid(row=1, column=2)




frame4 = Frame(frame1)
frame4.grid(row=3, column=0)

studInfo = Label(frame4, text="Assessment Marks")
studInfo.grid(row=0, column=1)
assignment = Label(frame4, text="                 Assignment:")
assignment.grid(row=1, column=1)
txtAssignEntry = Entry(frame4)
txtAssignEntry.grid(row=1, column=2)
formalTest = Label(frame4, text="                 Formal Test:")
formalTest.grid(row=2, column=1)
txtFTEntry = Entry(frame4)
txtFTEntry.grid(row=2, column=2)
practical = Label(frame4, text="                       Practical:")
practical.grid(row=3, column=1)
txtPTEntry = Entry(frame4)
txtPTEntry.grid(row=3, column=2)
interCollExa = Label(frame4, text="Internal Collage Exam:")
interCollExa.grid(row=4, column=1)
txtICEEntry = Entry(frame4)
txtICEEntry.grid(row=4, column=2)


frame5 = Frame(frame1)
frame5.grid(row=3, column=1)

progressR = Label(frame5, text="Progress Report")
progressR.grid(row=0, column=1)
name = Label(frame5, text="                     Name:    ")
name.grid(row=1, column=1)
txtNameEntry = Entry(frame5)
txtNameEntry.grid(row=1, column=2)
studentNo = Label(frame5, text="           Student No:   ")
studentNo.grid(row=2, column=1)
txtStudNoEntry = Entry(frame5)
txtStudNoEntry.grid(row=2, column=2)
subject = Label(frame5, text="                   Subject:    ")
subject.grid(row=3, column=1)
txtSubEntry = Entry(frame5)
txtSubEntry.grid(row=3, column=2)
finalM = Label(frame5, text="             Final Mark:   ")
finalM.grid(row=4, column=1)
txtFMEntry = Entry(frame5)
txtFMEntry.grid(row=4, column=2)
remark = Label(frame5, text="    Remark (Rating):   ")
remark.grid(row=5, column=1)
txtRemarkEntry = Entry(frame5)
txtRemarkEntry.grid(row=5, column=2)

frame6 = Frame(frame1)
frame6.grid(row=0, column=0)





frame1.pack()
root.mainloop()
