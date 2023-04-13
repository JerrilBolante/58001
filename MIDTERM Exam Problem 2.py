from tkinter import *
class midtermExam2:
    def __init__(self,window):
        self.lbl1 = Label(window, text="Enter Given Name:")
        self.lbl1.place(x=100, y=50)
        self.txt1 = Entry(window, bd=3)
        self.txt1.place(x=300, y=50)
        self.lbl2 = Label(window, text="Enter Middle Name:")
        self.lbl2.place(x=100, y=80)
        self.txt2 = Entry(window, bd=3)
        self.txt2.place(x=300, y=80)
        self.lbl3 = Label(window, text="Enter Last Name:")
        self.lbl3.place(x=100, y=110)
        self.txt3 = Entry(window, bd=3)
        self.txt3.place(x=300, y=110)
        self.lbl4 = Label(window, text="My Full Name is:")
        self.lbl4.place(x=100, y=150)
        self.txt4 = Entry(window, bd=3, width=30)
        self.txt4.place(x=300, y=150)

        self.lbl5 = Label(window, text="My Full Name")
        self.lbl5.place(x=200, y=20)

        self.btnfull = Button(window, text="Show Full Name")
        self.btnfull.place(x=200, y=180)

        self.btnfull.bind('<Button-1>', self.full)

    def full(self,full):

            GivenName = self.txt1.get()
            MiddleName = self.txt2.get()
            LastName = self.txt3.get()
            result = GivenName, MiddleName, LastName
            self.txt4.insert(END, result)

window = Tk()
mywindow = midtermExam2(window)
window.geometry("500x300+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()


