'''
#Vong lap While 1
value=-1
while value<1 or value>10 :
    value=int(input("Nhap vao 1 so tu nhien tu 1 den 10: "))
print("Binh phuong so vua nhap la: ",value**2)

#Vong lap while 2
n=int(input("Nhap gia tri n: "))
x=1
s=0
while x<=n:
    s+=x
    x+=1
print("Sum = ",s)

#Vong lap for
n=int(input("Nhap 1 so: "))
s=0
if n%2==0:
    for i in range (2,n+1,2):
        s+=i
elif n%2!=0:
    for i in range (1,n+1,2):
        s+=i
print("Sum= ",s)

#break
n=int(input("Nhap gia tri n:"))
s=0
for i in range(n):
    s+=i
    i+=1
    if(s>15):
        break
print("Sum= ",s)

#In gia tri
for i in range (1,10):
    print(i,end=" ")

#While/else
#for/else tuong tu
count=0
sum=0
while count<5:
    val=float(input("Nhap 1 gia tri >0: "))
    if(val<=0):
        print("Nhap sai gia tri, thoat phan mem!")
        break
    else: 
        sum+=val
        count+=1
else: #Su dung khi ham while ket thuc bth chu khong phai ket thuc bang break
    print("Trung binh la: ",round(sum/count,2))

#Vong lap long nhau: Ve chu N

for i in range(n):
    for j in range(n):
        if(j==0 or i==j or j==(n-1)):
            print("*",end="")#Viết nối tiếp mà không xuống dòng (Nối duôi)
        else:
            print(" ",end="")
    print()

#Ve hinh tam giac
n=int(input("Nhap chieu cao: "))
i=0
while i<n:
    j=0
    while j<n:
        if(j==0 or j==i or i==n-1):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    i+=1    
    print()  

#Tính tổng dãy số
def giaithua(n): #Đệ qui tính giai thừa của n
    if n==0 or n==1:
        return 1
    else: 
        return n*giaithua(n-1)
s=0
input_str=input("Nhập x,n : ")
dimensions=[int(x) for x in input_str.split(',')]
x=dimensions[0] #input x
n=dimensions[1] #input n
for i in range(1,n+1):
    s+=x**i/giaithua(i)
print("S({0},{1})= {2}".format(x,n,round(s,2)))

#Xét xem 1 số có phải là số nguyên tố không. Nếu có thì hỏi người dùng có nhập nữa không hay kết thúc phần mềm
import math
def snt(x):
    count=0
    for i in range(1,x+1):
        if x%i==0: count+=1
    return count==2
print("Chương trình xét xem có phải là số nguyên tố không!")
while True:
    x=int(input("Nhập vào 1 số nguyên dương bất kì: "))
    if(snt(x)):
        print(x,"là số nguyên tố")
    else:
        print(x,"không phải là số nguyên tố")
    a='a'
    while a!='y' and a!='n':
        a=str(input("Bạn có muốn tiếp tục không (y/n): "))
    if(a=='y'):
        continue
    else:
        print("Kết thúc phần mềm!")
        break

#Xuất bảng cứu chương
for i in range(1,11):
    for j in range(2,10):
        print("{0:>1}*{1:>2}= {2:>2}".format(j,i,j*i),end="\t")
    print()

# Câu 6 vẽ hình
n=int(input("Nhập 1 số: "))

for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
print("#"*15)

for i in range(n):
    for j in range(n):
        if(j==n-1 or j==n-1-i or i==n-1):
            print("* ",end="")
        else: 
            print("  ",end="")
    print()
print("#"*15)

i=0
while i<2*n-1:
    j=0
    while j<2*n-1:
        if((j==0 and i<=n-1) or (j==2*n-2 and i>n-1) or i==n-1 or i==j):
            print("* ",end="")
        else:
            print("  ",end="")
        j+=1
    i+=1
    print()
'''
#Câu 7: tính tổng dãy số
def giaithua(x):
    if(x==0 or x==1):
        return 1
    else:
        return x*giaithua(x-1)
input_str=input("Nhập 2 số x,n: ")
arr=[int(x) for x in input_str.split(',')]
x=arr[0]
n=arr[1]
s=0
for i in range(1,n+1):
    s+=x**(2*i+1)/(giaithua(2*i+1))
print("S({0},{1})= {2}".format(x,n,round(s,2)))




    