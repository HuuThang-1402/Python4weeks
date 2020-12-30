'''
from tkinter import *
root=Tk()
root.title("http:/communityuni.com")
root.resizable(height=True,width=True)
root.minsize(height=300,width=500)
def makecenter(root):
    root.update_idletasks()
    width=root.winfo_width()
    height=root.winfo_height()
    x=(root.winfo_screenwidth()//2)-(width//2)
    y=(root.winfo_screenheight()//2)-(height//2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
makecenter(root)  
root.mainloop()

from tkinter import *
root=Tk()
root.title("Hoc control co ban")
root.resizable(height=True,width=True)
root.minsize(height=300,width=400)
Label(root,text="Hello Tkinter",fg="blue").pack()
Button(root,text="click me",command=root.quit).pack()
e=StringVar()
e.set('http://communityuni.com')
Entry(root,textvariable=e,width=30).pack()
root.mainloop()

from tkinter import *
def tiepAction():
    StringA.set("")
    StringB.set("")
    StringRS.set("")
def giaiAction():
    a=float(StringA.get())
    b=float(StringB.get())
    if a==0 and b==0:
        StringRS.set("Vô số nghiệm")
    elif a==0:
        StringRS.set("Vô nghiệm")
    else:
        StringRS.set("x="+str(-b/a))
root=Tk()
StringA=StringVar()
StringB=StringVar()
StringRS=StringVar()
root.title("PTB1-Nguyễn Hữu Thắng")
root.resizable(height=True,width=True)
root.minsize(height=150,width=250)
Label(root,text="Phương trình bậc 1",fg='blue',font=('tohoma',20),justify=CENTER).grid(row=0,columnspan=2)
Label(root,text="Hệ số a:").grid(row=1,column=0)
Entry(root,width=30,textvariable=StringA).grid(row=1,column=1)
Label(root,text="Hệ số b:").grid(row=2,column=0)
Entry(root,width=30,textvariable=StringB).grid(row=2,column=1)

frameButton=Frame()
Button(frameButton,text="Giải",command=giaiAction).pack(side=LEFT)
Button(frameButton,text="Tiếp",command=tiepAction).pack(side=LEFT)
Button(frameButton,text="Thoát",command=root.quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)

Label(root,text="Kết quả:").grid(row=4,column=0)
Entry(root,width=30,textvariable=StringRS).grid(row=4,column=1)

root.mainloop()

from tkinter import *
def contiaction():
    StringA.set("")
    StringB.set("")
    StringC.set("")
    StringRS.set("")
    Stringx1.set("")
    Stringx2.set("")
def soluaction():
    a=float(StringA.get())
    b=float(StringB.get())
    c=float(StringC.get())
    delta=b*b-4*a*c
    if delta<0: StringRS.set("Phương trình vô nghiệm")
    elif delta==0:
        StringRS.set("Phương trình có 1 nghiệm kép")
        Stringx1.set(-b/(2*a))
    else:
        StringRS.set("Phương trình có 2 nghiệm phân biệt")
        Stringx1.set((-b+delta**0.5)/(2*a))
        Stringx2.set((-b-delta**0.5)/(2*a))
root=Tk()
StringA=StringVar()
StringB=StringVar()
StringC=StringVar()
StringRS=StringVar()
Stringx1=StringVar()
Stringx2=StringVar()
root.title("PTB2-HT")
root.resizable(height=True,width=True)
root.minsize(height=200,width=300)

Label(root,text="Phương trình bậc 2",fg="blue",font=("tohoma",20),justify=CENTER).grid(row=0,column=0,columnspan=2)
Label(root,text="Hệ số a:").grid(row=1,column=0)
Entry(root,width=30,textvariable=StringA).grid(row=1,column=1)
Label(root,text="Hệ số b:").grid(row=2,column=0)
Entry(root,width=30,textvariable=StringB).grid(row=2,column=1)
Label(root,text="Hệ số c:").grid(row=3,column=0)
Entry(root,width=30,textvariable=StringC).grid(row=3,column=1)

frameButton=Frame()
Button(frameButton,text="Giải",command=soluaction).pack(side=LEFT)
Button(frameButton,text="Tiếp",command=contiaction).pack(side=LEFT)
Button(frameButton,text="Thoát",command=root.quit).pack(side=LEFT)
frameButton.grid(row=4,columnspan=2)

Label(root,text="Kết quả:").grid(row=5,column=0)
Entry(root,width=30,textvariable=StringRS).grid(row=5,column=1)
Label(root,text="x1 =").grid(row=6,column=0)
Entry(root,width=30,textvariable=Stringx1).grid(row=6,column=1)
Label(root,text="x2 =").grid(row=7,column=0)
Entry(root,width=30,textvariable=Stringx2).grid(row=7,column=1)
root.mainloop()

from tkinter import *
def Addaction():
    a=float(StringA.get())
    b=float(StringB.get())
    StringRS.set(a+b)
def Subaction():
    a=float(StringA.get())
    b=float(StringB.get())
    StringRS.set(a-b)
def Mulaction():
    a=float(StringA.get())
    b=float(StringB.get())
    StringRS.set(a*b)
def Divaction():
    a=float(StringA.get())
    b=float(StringB.get())
    if b==0: StringRS.set("Can't div a by b")
    else: StringRS.set(a/b)
def conti():
    StringA.set("")
    StringB.set("")
    StringRS.set("")
root=Tk()
StringA=StringVar()
StringB=StringVar()
StringRS=StringVar()
root.title("TK")
root.resizable(height=True,width=True)
root.minsize(height=150,width=220)
Label(root,text="Add Sub Mul Div",font=("tohoma",16),justify=CENTER).grid(row=0,columnspan=3)
frameButton=Frame()
Button(frameButton,text="Add",command=Addaction).pack(side=TOP,fill=X)
Button(frameButton,text="Sub",command=Subaction).pack(side=TOP,fill=X)
Button(frameButton,text="Mul",command=Mulaction).pack(side=TOP,fill=X)
Button(frameButton,text="Div",command=Divaction).pack(side=TOP,fill=X)
frameButton.grid(row=1,column=0,rowspan=4)

Label(root,text="Number a:").grid(row=1,column=1)
Entry(root,width=15,textvariable=StringA).grid(row=1,column=2)
Label(root,text="Number b:").grid(row=2,column=1)
Entry(root,width=15,textvariable=StringB).grid(row=2,column=2)
Label(root,text="Result:").grid(row=3,column=1)
Entry(root,width=15,textvariable=StringRS).grid(row=3,column=2)
Button(root,text="Continue",command=conti).grid(row=4,column=1)
Button(root,text="Exit",command=root.quit).grid(row=4,column=2)

root.mainloop()
'''
from tkinter import *
def Add1():
    a=str(StringA.get())
    a+="1"
    StringA.set(a)
def Add2():
    a=str(StringA.get())
    a+="2"
    StringA.set(a)
def Add3():
    a=str(StringA.get())
    a+="3"
    StringA.set(a)
def Add4():
    a=str(StringA.get())
    a+="4"
    StringA.set(a)
def Add5():
    a=str(StringA.get())
    a+="5"
    StringA.set(a)
def Add6():
    a=str(StringA.get())
    a+="6"
    StringA.set(a)
def Add7():
    a=str(StringA.get())
    a+="7"
    StringA.set(a)
def Add8():
    a=str(StringA.get())
    a+="8"
    StringA.set(a)
def Add9():
    a=str(StringA.get())
    a+="9"
    StringA.set(a)
def Add0():
    a=str(StringA.get())
    a+="0"
    StringA.set(a)
def Addpoint():
    a=str(StringA.get())
    a+="."
    StringA.set(a)
def EqualAction():
    a=str(StringA.get())
    b,c,d=0,0,0
    for i in range(len(a)):
        if a[i]=="/":
            b=i                                                
            for j in range(i+1,len(a)):
                if a[j] in ("+","-","*","/"):
                    c=j
                    break
                elif j==len(a)-1:c=j+1
        if b!=0:
            if int(a[b+1:c])==0: 
                d+=1
                break
    if d==1: StringA.set("Math Error!!!")
    else:StringA.set(eval(a))
def Addadd():
    a=str(StringA.get())
    a+="+"
    StringA.set(a)
def Addsub():
    a=str(StringA.get())
    a+="-"
    StringA.set(a)
def Addmul():
    a=str(StringA.get())
    a+="*"
    StringA.set(a)
def Adddiv():
    a=str(StringA.get())
    a+="/"
    StringA.set(a)
def conti():
    StringA.set("")
root=Tk()
root.title("TK")
StringA=StringVar()
StringRs=StringVar()
root.resizable(height=True,width=True)
root.minsize(height=180,width=150)
Entry(root,width=25,textvariable=StringA).grid(row=0,columnspan=5)
Button(root,text="1",width=25//4,command=Add1).grid(row=1,column=0)
Button(root,text="2",width=25//4,command=Add2).grid(row=1,column=1)
Button(root,text="3",width=25//4,command=Add3).grid(row=1,column=2)
Button(root,text="4",width=25//4,command=Add4).grid(row=2,column=0)
Button(root,text="5",width=25//4,command=Add5).grid(row=2,column=1)
Button(root,text="6",width=25//4,command=Add6).grid(row=2,column=2)
Button(root,text="7",width=25//4,command=Add7).grid(row=3,column=0)
Button(root,text="8",width=25//4,command=Add8).grid(row=3,column=1)
Button(root,text="9",width=25//4,command=Add9).grid(row=3,column=2)
Button(root,text="-",width=25//4,command=Addsub).grid(row=4,column=0)
Button(root,text="0",width=25//4,command=Add0).grid(row=4,column=1)
Button(root,text=".",width=25//4,command=Addpoint).grid(row=4,column=2)
frameButton=Frame()
Button(frameButton,text="+",width=25//7,command=Addadd).pack(side=LEFT,fill=X)
Button(frameButton,text="-",width=25//7,command=Addsub).pack(side=LEFT,fill=X)
Button(frameButton,text="*",width=25//7,command=Addmul).pack(side=LEFT,fill=X)
Button(frameButton,text="/",width=25//7,command=Adddiv).pack(side=LEFT,fill=X)
Button(frameButton,text="=",width=25//7,command=EqualAction).pack(side=LEFT,fill=X)
frameButton.grid(row=5,column=0,columnspan=5)
Button(root,text="Clear",width=20,command=conti).grid(row=6,columnspan=5)
root.mainloop()
