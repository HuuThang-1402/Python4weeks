'''
import math
f=lambda:int(input())
d,x,y=f(),f(),f()
if d<=x:r=1
elif x<=y:r="Impossible"
else:r=math.ceil((d-x)/(x-y))+1
print(r)

n, c0, c1 = input().split()
n = int(n)
a=[]
for i in range(n):
    a.append('{:b}'.format(int(input())))
l = max(len(x) for x in a)
for x in a:
    print(x.zfill(l).replace('0', c0).replace('1', c1))

n=int(input())
for i in range(n):h,m,s=map(int,input().split(":"));g=s//60;m+=g;s-=g*60;g=m//60;h+=g;m-=g*60;print("%02d:%02d:%02d"%(h,m,s))

b, t = [int(j) for j in input().split()]

input1 = input()
a=input1.replace(",",".")
b=a.replace(".","").replace("-","")
if b.isdigit() and a.count(".")<2 and a.count("-")<1:
    print("Value:",input1)
    if float(a)>0:print("Sign: Positive")
    elif float(a)<0: print("Sign: Negative")
    else: print("Neutral")
    b=0
    for i in input1:
        if i.isdigit():b+=1
    print("Precision:",b)
    c=0
    for i in range(len(a)):
        if a[i]=="." or a[i]==",":
            c=len(a)-i+1
            break
    print("Scale:",c)
else: print("Invalid")

n, k = [int(i) for i in input().split()]
sol=[]
for i in range(int(n/k)):
    sol.append(k)
    n-=k
if n != 0:
    sol.append(n)
print(*sol)

from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Style
from tkinter.ttk import Entry
 
class Example(Frame):
  
 def __init__(self, parent):
   Frame.__init__(self, parent) 
  
   self.parent = parent
   self.initUI()
 
  
 def initUI(self):
  
   self.parent.title("Calculator")
  
   Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
  
   self.columnconfigure(0, pad=3)
   self.columnconfigure(1, pad=3)
   self.columnconfigure(2, pad=3)
   self.columnconfigure(3, pad=3)
  
   self.rowconfigure(0, pad=3)
   self.rowconfigure(1, pad=3)
   self.rowconfigure(2, pad=3)
   self.rowconfigure(3, pad=3)
   self.rowconfigure(4, pad=3)
  
   entry = Entry(self)
   entry.grid(row=0, columnspan=4, sticky=W+E)
   cls = Button(self, text="Cls")
   cls.grid(row=1, column=0)
   bck = Button(self, text="Back")
   bck.grid(row=1, column=1)
   lbl = Button(self)
   lbl.grid(row=1, column=2) 
   clo = Button(self, text="Close")
   clo.grid(row=1, column=3) 
   sev = Button(self, text="7")
   sev.grid(row=2, column=0) 
   eig = Button(self, text="8")
   eig.grid(row=2, column=1) 
   nin = Button(self, text="9")
   nin.grid(row=2, column=2) 
   div = Button(self, text="/")
   div.grid(row=2, column=3) 
   
   fou = Button(self, text="4")
   fou.grid(row=3, column=0) 
   fiv = Button(self, text="5")
   fiv.grid(row=3, column=1) 
   six = Button(self, text="6")
   six.grid(row=3, column=2) 
   mul = Button(self, text="*")
   mul.grid(row=3, column=3) 
  
   one = Button(self, text="1")
   one.grid(row=4, column=0) 
   two = Button(self, text="2")
   two.grid(row=4, column=1) 
   thr = Button(self, text="3")
   thr.grid(row=4, column=2) 
   mns = Button(self, text="-")
   mns.grid(row=4, column=3) 
  
   zer = Button(self, text="0")
   zer.grid(row=5, column=0) 
   dot = Button(self, text=".")
   dot.grid(row=5, column=1) 
   equ = Button(self, text="=")
   equ.grid(row=5, column=2) 
   pls = Button(self, text="+")
   pls.grid(row=5, column=3)
  
   self.pack()
 
root = Tk()
app = Example(root)
root.mainloop()

arr=[]
n = int(input())
for i in range(n):
    name, x, y, z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    arr.append([name,x,y,z])
arr1,arr2,arr3,arr4=[],[],[],[]
for i in arr:
    if i[1]==i[2]==i[3]: 
        if arr1==[]:arr1.append(i)
        else: 
            if i[1]>arr1[len(arr1)-1][1]: arr1.append(i)
    else:
        a=i[1:4]
        a.sort()
        for j in range(3):
            i[j+1]=a[j]
        print(i)
        if i[3]-i[2]==i[2]-i[1]==1:
            if arr2==[]:arr2.append(i)
            else: 
                if i[3]>=arr2[len(arr1)-1][3]: arr2.append(i)
        else:
            if i[1]==i[2] or i[2]==i[3]: 
                if i[2]==i[3]:
                    i[3]=i[1]
                    i[1]=i[2]
                if arr3==[]:arr3.append(i)
                else: 
                    if i[1]>arr3[len(arr3)-1][1]: arr3.append(i)
                    elif i[1]==arr3[len(arr3)-1][1]:
                        if i[3]>=arr3[len(arr3)-1][3]:arr3.append(i)
            else:
                if arr4==[]: arr4.append(i)
                else: 
                    if i[3]>arr4[len(arr4)-1][3]:arr4.append(i)
                    elif i[3]==arr4[len(arr4)-1][3]:
                        if i[2]>arr4[len(arr4)-1][2]:arr4.append(i)
                        elif i[2]==arr4[len(arr4)-1][2]:
                            if i[1]>=arr4[len(arr4)-1][1]:arr4.append(i)
if arr1!=[]: print(arr1[len(arr1)-1][0])
elif arr2!=[]: 
    if len(arr2)!=1 and arr2[len(arr2)-1][3]==arr2[len(arr2)-2][3]: print("Draw")
    else:print(arr2[len(arr2)-1][0])
elif arr3!=[]:
    if len(arr3)!=1 and arr3[len(arr3)-1][1]==arr3[len(arr3)-2][1] and arr3[len(arr3)-1][3]==arr3[len(arr3)-2][3]: print("Draw")
    else: print(arr3[len(arr3)-1][0])
elif arr4!=[]:
    if len(arr4)!=1 and arr4[len(arr4)-1][1]==arr4[len(arr4)-2][1]: print("Draw")
    else: print(arr4[len(arr4)-1][0])

orders = input()
orders=orders.replace("up","^").replace("down","v").replace("right",">").replace("left","<").split()
orders.append(0)
i=0
while i<len(orders):
    for j in range(i+1,len(orders)):
        if orders[j]!=orders[i]: 
            if j-i==1:print(orders[i],end="")
            else: print(orders[i]+str(j-i),end="")
            i=j-1
            break
    i+=1

a,b=0,0
for i in range(int(input())):
    s = input()
    for i in range(len(s)):
        if s[i]=="A":
            a=s[:i].count("\\","/")
        if s[i]=="B":
            b=s[:i].count("\\","/")
print(a,b)
print(a%2==b%2)

n,m=map(int,input().split())
for i in range(n):
    v=input()
    if sum(int(x)for x in v[:-2])!=int(v[-2:]):print("Agent",i+1);exit()
print("No traitors")

a=[]
h = int(input())
l = int(input())
for i in range(h):
    a.append(input())
for i in range(len(a)):
    j=a[i].find("B")
    if j!=-1:
        if "C" in (a[i][j-1],a[i][j+1],a[i+1][j],a[i-1][j]):print("BRIAN IS IN THE CORRIDOR")
        elif "E"in (a[i][j-1],a[i][j+1],a[i+1][j],a[i-1][j]): print("BRIAN IS IN THE BEDROOM")
        elif "L"in (a[i][j-1],a[i][j+1],a[i+1][j],a[i-1][j]):print("BRIAN IS IN THE LIVING ROOM")
        elif "K"in (a[i][j-1],a[i][j+1],a[i+1][j],a[i-1][j]):print("BRIAN IS IN THE KITCHEN")
        elif "T"in (a[i][j-1],a[i][j+1],a[i+1][j],a[i-1][j]):print("BRIAN IS IN THE BATHROOM")
        else:print("BRIAN IS NOWHERE")
        exit()
    
n=int(input())+1
f=lambda n:bin(n).count("1")
x=f(n-1)
while(f(n)!=x):n+=1
print(n)

n = int(input())
b=["GA","BU","ZO","MEU"]
arr=[]
while n>3:
    a=n%4
    arr.append(b[a])
    n//=4
arr.append(b[n])
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end="")

k = int(input())
a=[1]*4
b=1
for i in range(k//2):
    for j in range(len(a)):
        a[j]=a[j]+(2*(j+1)+8*i)
        b+=a[j]
print(b)

import math
a,b=map(int,input().split())
if a**b<100:print(a**b)
else: 
    n=math.ceil(b*math.log(a,10))
    print(int(10**(b*math.log(a,10)-n+3)))

n = input()
n+="1"
arr=[]
i=0
while i<len(n):
    if n[i]=="0":
        for j in range(i+1,len(n)):
            if n[j]!="0":
                if arr==[]: arr.append(j-i)
                else: 
                    print(i,j)
                    if (j-i)>arr[len(arr)-1]: arr.append(j-i)
                i=j-1
                break
    i+=1
if arr==[]: print(0)
else:
    print(arr)
    print(arr[len(arr)-1])

n = int(input())
arr=[]
for i in range(n):
    arr1=[]
    for j in input().split():
        arr1.append(j)
    arr.append(arr1)
a=0
for i in range(len(arr)):
    a=a+int(arr[i][i])+int(arr[i][len(arr[i])-1-i])
if len(arr)%2==1:print(a-int(arr[len(arr)//2][len(arr)//2]))
else: print(a)

I=input
s=list(I())
t=list(I())
for i in range(len(s)):
 if s[i]!=t[i]:print(*s,sep='');s[i]=t[i]
print(*t,sep='')

n = int(input())
for i in range(n-1,-1,-1):
    a=0
    for j in range(n-1,i-1,-1):
        print(" "*(i)+"/"+" "*(2*(n-1-i-a))+"\\"+" "*(i+j+a-(n-1)),end="")
        a+=1
    print()

b,w,x,y,z=[int(i) for i in input().split()]
print(b*x+w*y+min(b*(y-x+z),w*(x-y+z),0))

s=input();print(f"({s[:3]}) {s[3:6]}-{s[6:]}")

n = int(input())
a=n//6
if a*6==n: print(a);exit()
for i in range(a,0,-1):
    b=n-i*6
    for j in range(1,b//9+1):
        if (b-9*j)%20==0:
            print(i+j+(b-9*j)//20);exit()
print("NONE")

r=int(input())
c=int(input())
d=len(str((r*c-1)))
for i in range(r):
    print(end=" ")
    for j in range(c):
        a=str(j+i*c)
        if j!=c-1:print(a.rjust(d),end=" ")
        else:print(a.rjust(d))

n, x = [int(i) for i in input().split()]
w = [0] * x
for i in range(n):
    a, b = [int(j) for j in input().split()]
    for j in range(a, b+1):
        w[j]+=1
print(w)
print(min(w))
print(max(w))
'''
