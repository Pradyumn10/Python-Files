from tkinter import*
from tkinter import messagebox
top=Tk()
top.geometry("350x300")
c=Canvas(top,bg="black",height=1000,width=1050)
c.pack()
head=Label(text="Login",bg="skyblue").place(x=150,y=50)
user=Label(text="Username",bg="skyblue").place(x=60,y=100)
user1=Entry(width=20,bg="skyblue").place(x=150,y=100)
pas=Label(text="Password",bg="skyblue").place(x=60,y=150)
pas1=Entry(width=20,bg="skyblue").place(x=150,y=150)
but=Button(text="Submit",bg="skyblue").place(x=130,y=200)
messagebox.showinfo("information","Login Successful")
top.mainloop()
