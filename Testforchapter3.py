"""
#So sanh 2 so thuc 
d1=2.11-2.10
d2=1.10-1.09
print("d1= ",d1,"d2= ",d2)
diff=d1-d2 #Sai so
if diff<0:
    diff=-diff
if diff<0.0000001:
    print("d1 bang d2")
else:
    print("d1 khac d2 ")

#if else expression
a=5
b=7
if a==b:
    c=113
else:
    c=115
print(c)
c=113 if a==b else 115
print(c)
x=int(input("Nhap vao 1 so x: "))
print("x la so chan" if x%2==0 else "x la so le")

#Bai tap nam nhuan
x=int(input("Nhap vao 1 nam: "))
if x<0 :
    print("Ban da nhap sai nam")
else: 
    if((x%4==0 and x%100!=0) or x%400==0):
        print("Nam",x, "la nam nhuan")
    else:
        print("Nam",x," khong la nam nhuan")

#Bai tap dem so ngay trong thang
import numpy as np
month=int(input("Input the month: "))
if(month<1 or month >12):
    print("The error input")
else:
    if(month in (1,3,5,7,8,10,12)):
        print("Thang",month,"co 31 ngay")
    elif(month in (4,6,9,11)):
        print("Thang",month,"co 30 ngay")
    else:
        year=int(input("Input the year: "))
        if year<0 :
            print("Ban da nhap sai nam")
        else: 
            if((year%4==0 and year%100!=0) or year%400==0):
                print("Thang 2 nam",year,"co 29 ngay")
            else:
                print("Thanh 2 nam",year,"co 28 ngay")
"""
#Cau 3: Doc so
def chuc(x):
    switcher={
        1:'Mười',
        2:'Hai mươi',
        3:'Ba mươi',
        4:'Bốn mươi',
        5:'Năm mươi',
        6:'Sáu mươi',
        7:'Bảy mươi',
        8:'Tám mươi',
        9:'Chín mươi',
        0:''
    }
    return switcher.get(x,"Invalid input")
def donvi(x):
    switcher={
        1:'mốt',
        2:'hai',
        3:'ba',
        4:'bốn',
        5:'lăm',
        6:'sáu',
        7:'bảy',
        8:'tám',
        9:'chín',
        0:''
    }
    return switcher.get(x,"Invalid input")
x=int(input("Nhập vào số có 2 chữ số: "))
j=[]
if x in range(1,100):
    a=x//10
    j.append(chuc(a)) #Thêm chuỗi vào cuối hàng
    b=x%10
    if(a==1 or a==0): #Đọc các số: 1, 5, 11.
        if (b==1):
            j.append('một')
        elif(b==5 and a==0):
            j.append('năm')
        elif(b==5 and a==1):
            j.append('lăm')
        else:
            j.append(donvi(b))
    else:
        j.append(donvi(b))
elif (x==0):
    a=0
    j.append('Không')
else:
    a=0
    j.append('Invalid input')
if(a==0):
    print (''.join(j).title())
else:
    print (' '.join(j))

"""
#Cau 4
day=int(input("Input the day: "))
month=int(input("Input the month: "))
year=int(input("Input the year: "))
if(year<0):
    print("Invalid input!")
elif(month in (1,3,5,7,8,10,12)):
    if(day<1 or day>31):
        print("Invalid input!")
    else:
        day+=1
        if(day==32):
            day=1
            month+=1
            if(month==13):
                month=1
                year+=1
        print("Ngày kế tiếp là:",day,"/",month,"/",year)        
elif(month in (4,6,9,11)):
    if(day<1 or day>30):
        print("Invalid input!")
    else:
        day+=1
        if(day==31):
            day=1
            month+=1
        print("Ngày kế tiếp là:",day,"/",month,"/",year)
elif(month==2):
    if((year%4==0 and year%100!=0) or year%400==0):
        if(day<1 or day>29):
            print("Invalid input!")
        else:
            day+=1
            if(day==30):
                day=1
                month+=1
            print("Ngày kế tiếp là:",day,"/",month,"/",year)
    else:
        if(day<1 or day>28):
            print("Invalid input!")
        else:
            day+=1
            if(day==29):
                day=1
                month+=1
            print("Ngày kế tiếp là:",day,"/",month,"/",year)
else:
    print("Invalid input!")
"""