'''
q=s=0
for i in input():
    if i.isnumeric()==True:
        q=0
    elif i.isnumeric()==False and i==".":
        q+=1       
    else:s+=1
print(q,s)
print("integer"if (q<1 and s<1) else"float"if q==1 else"string")
#q=0 co 0 dau cham q=1 and s=0 co 1 dau cham s=1 co 2 dau cham

#In ra nghiem nguyen to nho nhat
from math import sqrt
def isPrime(x):
    count=0
    if x==2 or x==3:
        count=1
    else:
        b=int(sqrt(x))
        for i in range(2,b+1):
            if(x%i==0):
                count=0
                break
            else:
                count+=1
    if(count==0):
        return False
    else:
        return True
n = int(input())
if(n<2):
    print("NONE")
for i in range(2,n+1):
    if(n%i==0 and isPrime(i)==True):
        print(i)
        break
#n=int(input())
#print("NONE" if n<2 else min(i for i in range(2,n+1) if n%i<1))


# dem so so co trong doan 
n = int(input())
value=[]
for i in range(n):
    count=0
    for j in input():
        if(j.isdigit()):
            count+=1
    value.append(str(count))
print ('\n'.join(value))

#cho man hinh cheo va ti le
n = float(input())
w,h = map(float,input().split(":"))
x=(w*w+h*h)**.5
ww = n*(w/x)
hh = n*(h/x)
print(f"{ww:.2f} x {hh:.2f}")

l=[]
n=int(input())
for i in range(n):
    s=[int(c)for c in input().split()]
    if i==0 or i==n-1:
        [l.append(k)for k in s]
    else:
        l.append(s[0])
        l.append(s[-1])
print(sum(l))


for i in s: 
    if i.islower():print(i.upper(),end='')
    else:print(i.lower(),end='')

#AAA
#BBB
#AAA
#3A3B3A
arr=[]
n = int(input())
for i in range(n):
    a=0
    s=input()
    j=0
    while(j<n):
        count=0
        if j!=n-1:
            if s[j]!=s[j+1]:
                arr.append(s[j])
            else:
                for k in range(j+1,n):
                    count+=1
                    if(s[k]!=s[j]):
                        count-=1
                        break            
                arr.append(str(count+1))
                arr.append(s[j])
                j+=count
                if(j==n-1):
                    a=1
        else:
            if(a==0):
                arr.append(s[n-1])
        j+=1
print(''.join(arr))
lower
arr=[]
word = input()
n=len(word)
count=n
for i in range(0,n,2):
    arr.append(word[i//2])
    arr.append(word[n-1-i//2])
print(''.join(arr))

[print(sum(map(ord,i)))for i in input().split()] #trả về kí tự mã ascii
import sys
import math
n = int(input())
arr=[]
for i in range(n):
    a = int(input())
    arr.append(str(a))
count=0
op=True
i=0
while op:
    temp=int(arr[i])
    i=temp
    count+=1
    if i==0 or count==n-1: 
        op=False
if(i==0):
    print("true")
else:
    print("false")

import sys
import math

count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i**j==n:
            count+=1
            break
if(count!=0):
    print("Perfect")
else:
    print("Flawed")

import sys
import math 
n = int(input())
s = [str(x) for x in input().split(' ')]
count=0
op=True
while op:
    if(s[n-1]!='0'):
        n=int(s[n-1])
        count+=1
    else: op=False
print(count)

m = input()
m+=" "
arr=[]
arr1=[]
for i in range(len(m)):
    if m[i]==" ":
        arr1.append(str(i))
for i in range(int(arr1[0])):
    arr.append(m[i])
    arr.append(m[int(arr1[i])+1:int(arr1[i+1])+1])
print("".join(arr))

int(input())
for i in input().split(): print("[ ] "+i if int(i)%2==0 else "[x] "+i)

n = int(input())
lista=[]
a=0
for i in range(n):
    city, population = input().split()
    population = int(population)
    lista.append([city, population])

search = input()
for i in lista:
    if search in i[0]:
        a+=i[1]
print(a)

count=0
text = input()
moves = input()
for i in moves:
    if i==">": count+=1
    else : count-=1
for i in range(len(text)):
    if count>=0:
        i+=len(text)-count
        if i>=len(text)-1:
            i=i-len(text)
        print(text[i],end="")
    else:
        i-=len(text)+count
        if i<0:
            i=i+len(text)
        print(text[i],end="")

text = input()
moves = input()
k = 0
for i in moves:
    if i == '>':
        k-=1
    else:
        k+=1
print(text[k:]+text[:k])

n = int(input())
a=str(bin(n).replace("0b",""))
a=len(a)
for i in range(n):
    print(bin(i).replace("0b","").rjust(a))

arr=[]
c,s=input().split()
m=c.split(":")
n=s.split(":")
a=int(n[0])-int(m[0])
b=int(n[1])-int(m[1])
if (b<0):
    b+=60
    a-=1
print(str(a)+":"+str(b).rjust(2,"0"))

import math
n=int(input())
a=0
for i in range(1,n//5+1):
    k=5*i
    b=math.log(k,10)
    c=math.log(k,5)
    if b.is_integer():a+=b
    elif c.is_integer():a+=c
    else: a+=1
print(int(a))
'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a=input().split()
i,m,n=0,0,0
while i<len(a):
    if a[i][0].isdigit():print(*a[:i],end="|");m=i
    if a[i] in ["Street","Highway","Drive","Boulevard"]:print(*a[m:i+1],end="|");n=i+1
    if a[i].isupper():print(*a[n:i],end="|");print(a[i],end="|");print(a[i+1]);break
    i+=1

