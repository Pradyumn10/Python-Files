import math
from tkinter import*
window=Tk()
window.geometry("300x130")

def add(p,q):
    z=p+q
    print(z)

var1=1
a1=Button(text="1",width=10,textcommand=var1).grid(row=2,column=2)
a2=Button(text="2",width=10).grid(row=2,column=3)
a3=Button(text="3",width=10).grid(row=2,column=4)
a4=Button(text="4",width=10).grid(row=3,column=2)
a5=Button(text="5",width=10).grid(row=3,column=3)
a6=Button(text="6",width=10).grid(row=3,column=4)
a7=Button(text="7",width=10).grid(row=4,column=2)
a8=Button(text="8",width=10).grid(row=4,column=3)
a9=Button(text="9",width=10).grid(row=4,column=4)
a0=Button(text="0",width=10).grid(row=5,column=2)
a00=Button(text="00",width=10).grid(row=5,column=3)
a_cls=Button(text="cls",width=10).grid(row=5,column=4)
a_add=Button(text="+",width=10,command=add).grid(row=2,column=5)
a_sub=Button(text="-",width=10).grid(row=3,column=5)
a_mul=Button(text="*",width=10).grid(row=4,column=5)
a_div=Button(text="/",width=10).grid(row=5,column=5)
a_sin=Button(text="sin",width=10).grid(row=6,column=2)
a_cos=Button(text="cos",width=10).grid(row=6,column=3)
a_tan=Button(text="tan",width=10).grid(row=6,column=4)
window.mainloop()
