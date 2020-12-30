
#Bai1 
import math
c=50
h=30
value = []
items=[x for x in input("Nhập giá trị của d: ").split(',')] #input dau vao
for d in items:
    value.append(str(float(round(math.sqrt(2*c*float(d)/h,),2))))

print ('\n'.join(value))
'''
#Bai 3
items=[x for x in input("Nhập một chuỗi: ").split(',')]
items.sort()
print (','.join(items))

#Bai2
input_str = input("Nhập X, Y: ")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print (multilist)

#Bai3
items=[str(x) for x in input("Input str: ").split(',')]
print(','.join(sorted(items))) 

#Bai4
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print (sentence)

#Bai5
items=[str(x) for x in input("Nhap chuoi cach nhau boi khoang trang: ").split(" ")]
arr=[]
print(' '.join(sorted(items))) 
for i in items:
    if i not in arr:
        arr.append(i)
print(" ".join(sorted(arr)))
s = input("Nhập chuỗi của bạn: ")
words = [word for word in s.split(" ")]
print (" ".join(sorted(set(words))))

#Bai6
value = []
items=[x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)
print (','.join(value))

#Bai7
arr=[]
count=0
for x in range(1000,3001):
    a=x//1000
    b=(x-a*1000)//100
    c=(x-a*1000-b*100)//10
    d=(x-a*1000-b*100-c*10)
    if(a%2==0 and b%2==0 and c%2==0 and d%2==0):
        count+=1
        arr.append(str(x))
print(",".join(arr))
print(count)
count1=0
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
        count1+=1
print (",".join(values))
print(count1)

#Bai8
arr=str(input("Nhap vao 1 chuoi bat ki: "))
len1=len(arr)
count=0
count1=0
for i in range(len1):
    if(('a'<arr[i] and arr[i]<'z') or ('A'<arr[i] and arr[i]<'Z')):
        count+=1
    elif('0'<arr[i] and arr[i]<'9'):
        count1+=1
    else:
        continue
print("So chu cai la: ",count)
print("So so la: ",count1)
s = input("Nhập câu của bạn: ")

d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("Số chữ cái là:", d["LETTERS"])
print ("Số chữ số là:", d["DIGITS"])

#Bai9
sort
s= input("Nhập 1 chuỗi bất kì: ")
d={"LOWER":0,"UPPER":0}
for c in s:
    if c.isupper():
        d["UPPER"]+=1
    elif c.islower():
        d["LOWER"]+=1
    else:
        continue
print("Số chữ in thường là: ",d["LOWER"])
print("So chu in hoa la: ",d["UPPER"])

#Bai10
def tinh(x,n):
    if n==0 :
        return x
    else:
        return x*10**n+tinh(x,n-1)         
x=int(input("Nhap vao gia tri x: "))
s=0
for i in range(4):
    s+=tinh(x,i)
print("Sum=",s)
a = input("Nhập số a: ")
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )

print ("Tổng cần tính là: ",n1+n2+n3+n4)
'''
#Bai12
import sys
netAmount = 0

while True:
    s = input("Nhập nhật ký giao dịch: ")
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print (netAmount)
