from tkinter import* 
from tkinter import messagebox
top=Tk()
def mes():
    if not text1.get():
        messagebox.showinfo("Error","Empty Field")
    else:
        messagebox.showinfo("information","Registered")    

top.geometry("350x300")
c=Canvas(top,bg="black",height=1000,width=1050)
c.pack()
msg=Message(top,text="Welcome to registration form",bg="skyblue")
msg.pack()
text1=StringVar()
head=Label(text="Registeration Form",bg="skyblue").place(x=150,y=50)
name=Label(text="Name",bg="skyblue").place(x=60,y=100)
user1=Entry(width=20,bg="skyblue",textvariable=text1).place(x=150,y=100)
user=Label(text="Username",bg="skyblue").place(x=60,y=150)
pas1=Entry(width=20,bg="skyblue").place(x=150,y=150)
pas=Label(text="Password",bg="skyblue").place(x=60,y=200)
pas1=Entry(width=20,bg="skyblue").place(x=150,y=200)
but=Button(text="Submit",bg="skyblue",command=mes).place(x=130,y=250)
r1=Radiobutton(top,text="Male")
r1=Radiobutton(top,text="Female")
top.mainloop()
 
