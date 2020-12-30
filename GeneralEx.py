# General Exercise : Book management software
from tkinter import *
from FileProcessing import *
def addAction():
    line = stringID.get()+";"+stringTitle.get()+";"+stringYear.get()
    SaveFile(line)
    stringID.set("")
    stringTitle.set("")
    stringYear.set("")
    showBook()
def showBook():
    arrBook = ReadFile()
    listbox.delete(0,END)
    for item in arrBook:
        listbox.insert(END,item)
def myFilter():
    arrBook=ReadFile()
    for i in range(len(arrBook)):
        for j in range(len(arrBook)):
            a=arrBook[i]
            b=arrBook[j]
            if a[2]>b[2]:
                arrBook[i]=b
                arrBook[j]=a
    listbox.delete(0,END)
    for item in arrBook:
        listbox.insert(END,item)
root=Tk()
stringID = StringVar()
stringTitle = StringVar()
stringYear = StringVar()
root.title("Book Management")
root.minsize(height=300, width=320)
Label(root,text="Book Management",fg='blue',font=('cambria',16)).grid(row=0,columnspan=2)
listbox = Listbox(root,width=50)
listbox.grid(row=1,columnspan=2)
showBook()

Label(root,text="Book ID:").grid(row=2,column=0)
Entry(root,width=30,textvariable=stringID).grid(row=2,column=1)
Label(root,text="Book title:").grid(row=3,column=0)
Entry(root,width=30,textvariable=stringTitle).grid(row=3,column=1)
Label(root,text="Year of publication:").grid(row=4,column=0)
Entry(root,width=30,textvariable=stringYear).grid(row=4,column=1)

frameButton=Frame(root)
Button(frameButton,text="Add",command=addAction).pack(side=LEFT)
Button(frameButton,text="Search").pack(side=LEFT)
Button(frameButton,text="Filter",command=myFilter).pack(side=LEFT)
Button(frameButton,text="Exit",command=root.quit).pack(side=LEFT)
frameButton.grid(row=5,column=1)

root.mainloop()