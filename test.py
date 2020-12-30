"""
x="Oc cho" #Ghi chu 1 dong
print(x)
print(type(x))
x=5.5
print(type(x))
x=True
print(type(x))

'''
Ghi chus nhieu dongsdsjdn
sdfjsndjg
'''

x=complex(3,2) #so phuc
print(type(x))
print("thuc =",x.real,"ao =",x.imag)
x=5
y=5
print(x is not y)

#Bai08: Nhap du lieu tu ban phim
x=float(input("Input: "))
print("Output: ",x)
print(type(x))
def StrToBool(s):
    return s.lower() in ("true", "t", "yes", "1")
x=input("Input True/False: ")
x=StrToBool(x)
print(x)

#Bai09: Xuat du lieu
print("-"*15)
print("{0:>2} {1:>11}".format('STT','Gia Tri'))
print("-"*15)
print("{0:>2}{1:>13}".format(1,10**10))
print("{0:>2}{1:>13}".format(2,10**9))
print("{0:>2}{1:>13}".format(3,10**8))
print("{0:>2}{1:>13}".format(4,10**7))
print("{0:>2}{1:>13}".format(5,10**6))
print("{0:>2}{1:>13}".format(6,10**5))
print("{0:>2}{1:>13}".format(7,10**4))
print("{0:>2}{1:>13}".format(8,10**3))
print("{0:>2}{1:>13}".format(9,10**2))
print("{0:>2}{1:>13}".format(10,10**1))
for x in range(10):
    print("{0:>2}{1:>13}".format(x+1,10**(10-x)))
print('-'*15)
x='Nguyen Huu Thang'
a=len(x)
print("{0:>16}".format("Donal Trump"))
print("{0:>16}".format("Putin"))
print("{0:>16}".format("Obama"))
print("{0:>16}".format(x))

#Tính chu vi diện tích hình tròn
import math
try:
    r=float(input("Nhap vao ban kinh hinh tron: "))
    P=2*math.pi*r
    S=math.pi*r**2
    print("Gia tri dien tich hinh tron la: ",S)
    print("Gia tri chu vi hinh tron la: ",P)
except:
    print("Loi roi")

#Tinh gio phut giay
import math
x=int(input("Input the value: "))
hour=(x//3600)%24
minute=(x%3600)//60
second=(x%3600)%60
if(hour<12):
    print(hour,":",minute,":",second," AM")
else:
    print(hour-12,":",minute,":",second," PM")

#Tinh dtb lam tron 2 con so
toan=float(input("Nhap diem Toan: "))
hoa=float(input("Nhap diem hoa: "))
av=float(input("Nhap diem av: "))
dtb=(toan+hoa+av)/3
print("DTB: ",dtb)
print("DTB: ",round(dtb,2))
""
def isprime(a):
    if a > 1:
        for i in range(2,a):
            if a%i == 0:
                return False
        return True
    return False
t=[]
n = int(input())
for i in range(n):
    a = int(input())
    if isprime(a):
        t.append(a)
print(sum(t))
print (1)

def custom_sort(elem):
    return elem
arr=[]
l=[]
n = int(input())
for i in range(n):
    word = input()
    a=len(word)
    l.append(a)
    arr.append(word)
i=min(l)
j=max(l)
for k in range(i,j+1):
    for m in range(len(arr)):
        if len(arr[m])==k:
            print(arr[m])

c= int(input())
s= int(input())
a=int(round(c/s,2)*100)
print("#"*c+"."*(s-c)+" {0}%".format(a))
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
a1=[]
a2=[]
n = int(input())
for i in range(n):
    row = input()
    a1.append(row)
empty_line = input()
for i in range(n):
    row = input()
    a2.append(row)
for i in range(n):
    a3=[]
    for j in range(n):
        if a1[i][j]==".": 
            a3.append(a2[i][j])
        elif a1[i][j]==a2[i][j]:
            a3.append(a1[i][j])
        elif a2[i][j]==".":
            a3.append(a1[i][j])
        else :
            a3.append("X")
    print("".join(a3))

