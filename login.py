from tkinter import *

from tkinter import ttk

from PIL import ImageTk

from tkinter import messagebox

from tkinter import filedialog

import pymysql

import webbrowser

import os

import sys

import mysql.connector

class Login:

    def __init__(self,root):

        self.root=root

        self.root.title("Student Details")

        self.root.geometry("1366x800+0+0")

        self.root.resizable(False,False)

        self.studentlogin()

    def studentlogin(self):

        Frame_studentlogin=Frame(self.root,bg="white")

        Frame_studentlogin.place(x=0,y=0,height=700,width=1366)


        frame_input=Frame(self.root,bg="white")

        frame_input.place(x=320,y=130,height=450,width=350)


        label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),fg="black",bg="white")

        label1.place(x=75,y=20)


        label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label2.place(x=30,y=95)

        self.rollnumber_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

        self.rollnumber_txt.place(x=30,y=145,width=270,height=35)


        label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label3.place(x=30,y=195)

        self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

        self.password.place(x=30,y=245,width=270,height=35)


        btn1=Button(frame_input,text="forgot password?",command=self.forgotpassword,cursor='hand2',font=('calibri',10),bg='white',fg='black',bd=0)

        btn1.place(x=125,y=305)

        btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

        btn2.place(x=90,y=340)

        btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

        btn3.place(x=110,y=390)


    def login(self):

        if self.rollnumber_txt.get()=="" or self.password.get()=="":

            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:

            try:
                con=pymysql.connect(host='localhost',user='root',password='Sreethu@12345',database='mydata',port=4306)

                cur=con.cursor()

                cur.execute('select * from signup where rollnumber=%s and password=%s',(self.rollnumber_txt.get(),self.password.get()))

                row=cur.fetchone()

                if row==None:

                    messagebox.showerror('Error','Invalid Username And Password',parent=self.root)

                    self.loginclear()

                    self.rollnumber_txt.focus()

                else:
                    os.system('pharma.py')
 
                 

            except Exception as es:

                messagebox.showerror('Error',f'Error Due to : (str(es))',parent=self.root)
    
    def Register(self):

        Frame_login1=Frame(self.root,bg="white")

        Frame_login1.place(x=0,y=0,height=1000,width=1366)

        frame_input2=Frame(self.root,bg='white')

        frame_input2.place(x=320,y=130,height=1500,width=630)

        label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),fg="black",bg='white')

        label1.place(x=45,y=20)

        label2=Label(frame_input2,text="Fullname",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label2.place(x=30,y=95)

        self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input2,text="Specialization",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label3.place(x=30,y=195)

        self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry2.place(x=30,y=245,width=270,height=35)

        label4=Label(frame_input2,text="Branch",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label4.place(x=330,y=95)

        self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry3.place(x=330,y=145,width=270,height=35)

        label5=Label(frame_input2,text="Rollno",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label5.place(x=330,y=195)

        self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry4.place(x=330,y=245,width=270,height=35)

        label6=Label(frame_input2,text="Father Name",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label6.place(x=30,y=295)

        self.entry5=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry5.place(x=30,y=345,width=270,height=35)

        label7=Label(frame_input2,text="Mother Name",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label7.place(x=330,y=295)

        self.entry6=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry6.place(x=330,y=345,width=270,height=35)

        label8=Label(frame_input2,text="Phone Number",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label8.place(x=30,y=395)

        self.entry7=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry7.place(x=30,y=445,width=270,height=35)

        label9=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label9.place(x=330,y=395)

        self.entry8=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry8.place(x=330,y=445,width=270,height=35)

        label10=Label(frame_input2,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label10.place(x=30,y=495)

        self.entry9=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry9.place(x=30,y=545,width=270,height=35)

        label11=Label(frame_input2,text="Email Id",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label11.place(x=330,y=495)

        self.entry10=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

        self.entry10.place(x=330,y=545,width=270,height=35)

        btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

        btn2.place(x=200,y=600)

        btn3=Button(frame_input2,command=self.studentlogin,text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

        btn3.place(x=390,y=600)

    
    def register(self):

        if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="" or self.entry5.get()==""or self.entry6.get()==""or self.entry7.get()==""or self.entry8.get()==""or self.entry9.get()==""or self.entry10.get()=="":

            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif self.entry8.get()!=self.entry9.get():

            messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)

        else:

            try:

                con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=4306)

                cur=con.cursor()

                cur.execute("select * from signup where rollnumber=%s",self.entry4.get())

                row=cur.fetchone()

                if row!=None:

                    messagebox.showerror("Error","User already Exist,Please Login with your credentials",parent=self.root)

                    self.regclear()

                    self.entry.focus()
                else:
                    
                    cur.execute("insert into signup value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.entry.get(),self.entry2.get(),self.entry3.get(),self.entry4.get(),self.entry5.get(),self.entry6.get(),self.entry7.get(),self.entry8.get(),self.entry9.get(),self.entry10.get()))

                    con.commit()

                    con.close()

                    messagebox.showinfo("Success","Register Succesfull",parent=self.root)

                    self.regclear()

            except Exception as es:

                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

    def forgotpassword(self):


        Frame_Login2=Frame(self.root,bg="white")

        Frame_Login2.place(x=0,y=0,height=700,width=1366)

        frame_input3=Frame(self.root,bg='white')

        frame_input3.place(x=320,y=130,height=450,width=350)

        label1=Label(frame_input3,text="Forgot Password",font=('impact',28,'bold'),fg="black",bg='white')

        label1.place(x=45,y=20)

        label2=Label(frame_input3,text="Roll Number",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label2.place(x=30,y=95)

        self.rollnumber_txt=Entry(frame_input3,font=("times new roman",15,"bold"),bg='lightgray')

        self.rollnumber_txt.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input3,text="Email id",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label3.place(x=30,y=195)

        self.email_txt=Entry(frame_input3,font=("times new roman",15,"bold"),bg='lightgray')

        self.email_txt.place(x=30,y=245,width=270,height=35)

        btn4=Button(frame_input3,text="Change Password",command=self.Password,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

        btn4.place(x=90,y=340)

    def Password(self):

        if self.rollnumber_txt.get()=="" or self.email_txt.get()=="":

            messagebox.showerror("Error","All Fields Are Required",parent=self.root)


        else:

            try:

                con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="pythongui",port=4306)

                cur=con.cursor()

                cur.execute("select * from suji where rollnumber=%s and emailid=%s",self.rollnumber_txt.get(),self.email_txt.get())

                row=cur.fetchone()

                if row==None:

                    messagebox.showerror("Error","Please enter correct credential",parent=self.root)

                    self.passwordclear()

                    self.rollnumber_txt.focus()
                else:

                    self.update()

                   

                    self.passwordclear()

                    self.rollnumber_txt.focus()

                    con.close()

            except Exception as es:

                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)


    def update(self):

        Frame_Login2=Frame(self.root,bg="white")

        Frame_Login2.place(x=0,y=0,height=700,width=1366)

        frame_input4=Frame(self.root,bg='white')

        frame_input4.place(x=320,y=130,height=450,width=350)

        label1=Label(frame_input4,text="update",font=('impact',28,'bold'),fg="black",bg='white')

        label1.place(x=45,y=20)

        label2=Label(frame_input4,text="New Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label2.place(x=30,y=95)

        self.rollnumber_txt=Entry(frame_input4,font=("times new roman",15,"bold"),bg='lightgray')

        self.rollnumber_txt.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input4,text="Conform Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

        label3.place(x=30,y=195)

        self.email_txt=Entry(frame_input4,font=("times new roman",15,"bold"),bg='lightgray')

        self.email_txt.place(x=30,y=245,width=270,height=35)

        btn4=Button(frame_input4,text="Update",command=self.studentlogin,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

        btn4.place(x=90,y=340)   
       

    def regclear(self):

        self.entry.delete(0,END)

        self.entry2.delete(0,END)

        self.entry3.delete(0,END)

        self.entry4.delete(0,END)

        self.entry5.delete(0,END)

        self.entry6.delete(0,END)

        self.entry7.delete(0,END)

        self.entry8.delete(0,END)

        self.entry9.delete(0,END)

        self.entry10.delete(0,END)

    def loginclear(self):

        self.rollnumber_txt.delete(0,END)

        self.password.delete(0,END)

    def passwordclear(self):

        self.rollnumber_txt.delete(0,END)

        self.email_txt.delete(0,END)


root=Tk()

ob=Login(root)

root.mainloop()

