from tkinter import *
import tkinter.messagebox as tm
import sys
import os
import tkinter



class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)
        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "admin" and password == "admin":
            top=tkinter.Tk()
            top.geometry("300x300")

            def helloCallBack_1():
                os.system('python face.py')
            def helloCallBack_2():
                os.system('python Main.py')
            def helloCallBack_3():
                os.system('python face.py')
   

            B=tkinter.Button(top,text="face Detection ",command= helloCallBack_1)
            B.pack()
            B=tkinter.Button(top,text="Car Number Plate Detection ",command= helloCallBack_2)
            B.pack()
            B=tkinter.Button(top,text="Boundaries ",command= helloCallBack_3)
            B.pack()
            top.mainloop()
        else:
            tm.showerror("Login error", "Incorrect username")


root = Tk()
root.geometry("300x300")
lf = LoginFrame(root)
root.mainloop()