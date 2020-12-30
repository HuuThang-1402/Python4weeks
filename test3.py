'''
print(len(set(input().lower())))

from calendar import*
m=int(input())
print(monthrange(int(input()),m)[1])

import math
d, s = [int(i) for i in input().split()]
for i in range(d,0,-1):
    for j in range(9,0,-1):
        if s-j>=i-1:
            print(j,end="")
            s=s-j
            break

w=input()
for i in w:
    a=len(w)
    w=w.replace("vv","v")
    if len(w)==a:
        break
print(w.replace("v","w"))

count=-1
s = input().split()
for i in s:
    count+=1
    for j in range(len(i)-1,-1,-1):
        print (i[j],end="")
    if count!=len(s)-1:print(end=" ")

speed = int(input())
arr=[]
light_count = int(input())
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    a=float(distance/duration*3.6)
    arr.append(a)
for i in range(speed,0,-1):
    count=0
    for j in arr:
        if int(j//i)%2!=0:continue
        else: count+=1
    if count==light_count: 
        print(i)
        break

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
#arr=[[0 for _ in range(width)] for _ in range(height)]
arr=[]
for i in range(height):
    line = input()  # width characters, each either 0 or .
    arr.append(line)
for i in range(height):
    for j in range(width):
        if arr[i][j]=="0":
            print(j,i,end=" ")
            for k in range(j+1,width+1):
                if k==width: print(-1,-1,end=" ")
                else:
                    if arr[i][k]=="0":
                        print(k,i,end=" ")
                        break
            for k in range(i+1,height+1):
                if k==height: print(-1,-1)
                else:
                    if arr[k][j]=="0":
                        print(j,k)
                        break

arr1=[]
arr2=[]
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    arr1.append([n1,n2])
    arr1.append([n2,n1])
for i in range(e):
    ei = int(input())  # the index of a gateway node
    arr2.append(ei)
# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    for i in arr2:
        if [si,i] in arr1:
            print(si,i)
            break
    else: 
        for i in arr2:
            arr3=[]
            for j in arr1:
                if i in j:
                    for k in j:
                        arr3.append(str(k))
                    print(" ".join(arr3))
                    break
            break

arr=[]
n = int(input())
for i in range(n):
    expression = input()
    a1=""
    for j in expression:
        if j==">": j="<"
        elif j=="}": j="{"
        elif j=="]": j="["
        elif j==")": j="("
        a1+=j
    arr.append(a1)
for i in arr:
    j=0
    while j<len(i)-1:
        n=0
        if i[j] in ("<","{","[","("):
            k=len(i)-1
            while k>j:
                if i[k]==i[j]:
                    if i[j+1:k].count("<")%2!=0 or i[j+1:k].count("{")%2!=0 or i[j+1:k].count("[")%2!=0 or i[j+1:k].count("(")%2!=0:
                        print("false")
                        n=1
                        break
                    k=j+1
                    i=i[j+1:k]
                k-=1
        if n==1:break
        j+=1
    else: print("true")

r = int(input())
g = int(input())
b = int(input())
print('#'+hex(r)[2:].zfill(2).upper()+hex(g)[2:].zfill(2).upper()+hex(b)[2:].zfill(2).upper())

message = input().split()
g=""
for l in message:
    if l =="32":
        g+=" "
    else:
        g+=chr(int(l))
g=g.split()
h=[u[::-1]for u in g]
print(" ".join(h))

message = input()
arr=[]
l=int(len(message)**0.5)
res = ""
for i in range(l):
    for j in range(l):
        res += message[i + j * l] 
print(res)

arr=[]
n = int(input())
for i in input().split():
    arr.append(i)
a,b=0,0
for i in range(len(arr)-1):
    if int(arr[i])<int(arr[i+1]): 
        a+=1
    else: b+=1
print(a,b)
n = int(input())
prev = None
hi = 0
lo = 0
for i in input().split():
    s = int(i)
    if prev is not None:
        if s > prev:
            hi += 1
        else:
            lo += 1
    prev = s
print(hi, lo)

c = int(input())
s=set()
for i in input().split():
    n = int(i)
    if n%2:
        s.add(n**2)

print(*(x for x in sorted(s,reverse=1)))

a3=0
a1 = int(input())
a2 = int(input())
operator = input()
k = int(input())
if operator not in ("+","-","*","/"): print("ERROR")
else: 
    for i in range(3,k+1):
        if operator=="+":
            a3=a2+a1
        if operator=="-":
            a3=a2-a1
        if operator=="*":
            a3=a2*a1
        if operator=="/":
            a3=a2/a1
        a1=a2
        a2=a3
print(a3)

n = int(input())
s=[]
for i in range(1,int(n**(1/2))+1):
    if n%i==0:
        s.append([abs(n//i-i),i,n//i])
print("*".join([str(a) for a in sorted(sorted(s)[0][1:])]))

s = input().split()[::-1]
n = int(input())
ls = []
for i in s:
    ls += [n//int(i)]
    n = n%int(i)
# print(ls)
r = ""
for x,i in enumerate(ls):
    if i:
        r+= f"{i}x{s[x]} "
print(r[:-1])
#int(a,16)

arr=[]
text = input().lower()
for i in range(len(text)):
    for j in range(i+1,len(text)):
        arr1=""
        if text[j]==text[i]:
            for k in range(len(text)-j):
                if text[j+k]==text[i+k]:
                    arr1+=(text[i+k])
                else: break
        if arr==[]: arr.append(arr1)
        elif len(arr1)>len(arr[len(arr)-1]): arr.append(arr1)
if arr!=[""]: print(arr[len(arr)-1])
else: print("None")

n = int(input())
numbers = input().split()
if n%2==0:
    for i in range(0,len(numbers),2):
        if int(numbers[i])>int(numbers[i+1]): print(numbers[i+1],numbers[i],end=" ")
        else: print(numbers[i],numbers[i+1],end=" ")
else:
    for i in range(0,len(numbers)-1,2):
        if int(numbers[i])>int(numbers[i+1]): print(numbers[i+1],numbers[i],end=" ")
        else: print(numbers[i],numbers[i+1],end=" ")
    print(numbers[len(numbers)-1])
n = int(input())
numbers = list(map(int,input().split(" ")))
i = 0
while i < len(numbers)-1:
    if numbers[i] > numbers[i+1]:
        tmp = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1]= tmp
    i+=2
print(*numbers)

n = int(input())
for i in range(n):
    if i==n-1: print("*"*n,end=" ")
    else: print(" "*n,end=" ")
    for j in range(2*n-1):
        if i>=2*n-2-j or i>=j:
            print("*",end=" ")
        else: print(" ",end=" ")
    print()

for i in range(int(input())):
    a,b=map(int,input().split())
    f=0
    for j in range(a,b+1):s=sum(k for k in range(1,j+1)if j%k<1);f+=2*j-s if s<2*j else 0
    print(f)   

mode,a,b,r=input(),int(input()),int(input()),int(input())
if mode=='AND': print(str(a&b==r).lower())
if mode=='OR': print(str(a|b==r).lower())
if mode=='XOR': print(str(a^b==r).lower())
# print(mode,a,b,r)
import sys
b=sys.stdin.readlines()
m,b1,b2,r=b[0].strip(),*map(lambda x:int(x,2),b[1::])
if m=="AND":o=b1&b2
elif m=="OR":o=b1|b2
else:o=b1^b2
print(str(o==r).lower())

n = int(input())
print(f'x{n:x}b{n:b}o{n:o}')
print(hex(n)[1:],end="")
print(bin(n)[1:],end="")
print(oct(n)[1:],end="")

s=input()
print('VALID'if 2<len(s)<21 and s.isalnum()else'INVALID')

X = [int(i) for i in input().split()]
Y = [int(i) for i in input().split()]
X.sort()
Y.sort()

s=''
for x,y in zip(X,Y):
    s += '(%d, %d), ' % (x,y)

print(s[:-2])
'''