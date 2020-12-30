"""
#Bai1
import time
x=time.localtime() #Thoi gian hien tai
print(x[0]) #Nam hien tai
def Tuoi(namsinh):
    a=x[0]-namsinh
    if(a==0):
        print("Tuoi cua ban la: 1")
    elif(a<0):
        print("Tuoi chua ton tai")
    else:
        print("Tuoi cua ban la: ",a)
namsinh=int(input("Nhap vao nam sinh:"))
Tuoi(namsinh)

#Bai4
import math
x=float(input("Input x: "))
a=4*(x**2+10*x*math.sqrt(x)+3*x+1)
b=(math.sin(math.pi*x**2)+math.sqrt(x**2+1))/(math.exp(2*x)+math.cos(math.pi*x/4))
print("y1 = ",a)
print("y2 = ",b)

#Bai7
a= int(input("nhập số 1: ")) 
b= int(input("nhập số 2: "))
c= int(input("nhập số 3: ")) 
if a<b and b<c:
    print(a,b,c)
elif a<c and c<b:
    print(a,c,b)
elif b<a and a<c:
    print(b,a,c)
elif b<c and b<a:
    print (b,c,a)
elif c<b and b<a:
    print(c,b,a)
else:
    print(c,a,b)

#Bai8
a= int(input("nhập số 1: ")) 
b= int(input("nhập số 2: "))
c= int(input("nhập số 3: ")) 
d= int(input("nhập số 4: ")) 
max=a
if(max<b):
    max=b
if(max<c):
    max=c
if(max<d):
    max=d
print("Max: ",max)

#Bai9
def Bai3(a,b,c):
    if (a+b)>c and (a+c)>b and (b+c)>a and (a>0) and (b>0) and (c>0):
        if(a==b)and (b==c):
            return 0
        elif((a*b+b*b==c*c)and(a==b))or((a*a+c*c==b*b)and(a==c))or((c*c+b*b==a*a)and(c==b)):
            return 1
        elif(a==b)or(b==c)or(a==c):
            return 2
        elif((a*a==b*b+c*c)or(b*b==a*a+c*c)or(c*c==a*a+b*b)):
            return 3
        else:
            return 4
    else:
        return 5      
if __name__=="__main__":
    a=int(input("Nhap a :"))
    b=int(input("Nhap b :"))
    c=int(input("Nhap c :"))         
    r=['Tam giac deu','tam giac vuong can','tam giac can','tam giac vuong ','tam giac thuong','khong hop le']
    i=Bai3(a,b,c)
    print (r[i])

#Bai10
def Tinhtien(sokm):
    if(sokm<=0):
        a=0
    elif(sokm<=1):
        a=5000
    elif(sokm<=5):
        a=(sokm-5)*4500+5000
    elif(sokm<=120):
        a=(sokm-5)*3500+4500*4+5000
    else:
        a=(((sokm-5)*3500+4500*4+5000)*1/10)
    print("So tien phai tra la: ",a)
if __name__=="__main__":
    sokm=int(input("Nhap so km: "))
    Tinhtien(sokm)
"""
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# print(vowels.reverse())
# sort the vowels
vowels.sort(reverse=True)
 
# print vowels
print('Sorted list:', vowels)

