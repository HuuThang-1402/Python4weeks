'''
arr=[]
n = int(input())
for i in range(n):
    e = int(input())
    if(e!=-1):
        op=ord("z")
        op1=op-e
        arr.append(chr(op1))
    else:
        arr.append(" ")
print("".join(arr))

i=int(s,16)

import sys
import math
n = int(input())
a=str(n)
op=True
while op:
    count=0
    n+=1
    b=str(n)
    for i in a:
        for j in b:
            if(j==i):
                count=0
                break
            else:
                count+=1
        if(count==0):
            break
    if count!=0:
        op=False          
print(n)

import sys
import math
arr=[]
arr1=[]
n = int(input())
for k in range(n):
    names = [str(x) for x in input().split(' ')]
    for i in names:
        if(i in arr):
            continue
        else:
            arr.append(i)
            count=0
            for j in names:
                if (j==i):
                    count+=1
            count+=1
            if(count>n/2):
                arr1.append(i)
print(''.join(arr1))

#print(''.join([i+'p'+i if i in "aeiouAEIOU"else i for i in input()]))

s_1 = [int(x) for x in input().split(" ")]
s_2 = [int(x) for x in input().split(" ")]
a=len(s_1)
b=len(s_2)
arr=[]
if(a!=b):
    arr.append("Invalid")
else:
    for i in range(len(s_1)):
        a=s_1[i]+s_2[i]
        arr.append(str(a))
print(" ".join(arr))

count=0
sequence = input()
for i in sequence:
    if ('a'<=i and i<="z"):
        count+=ord(i)-ord('a')+1
    elif('A'<=i and i<='Z'):
        count+=ord(i)-ord('A')+1
        count*=2
a=count
count1=0
for j in range(1,100):
    a/=10**j
    count1+=1
    if(a<1):
        break
if(count<=10**6):
    print(count*10**(5-count1))
else:
    print(count//10**5)

count=0
n, m = [int(i) for i in input().split()]
s = int(input())
for i in range(n):
    row = input()
    for j in row:
        if j=='o':
            count+=1
if(m>n):
    max=m
else:
    max=n
if(count>=(max//s+1)):
    print(max)
else: 
    print(count*s)


n = int(input())
m = int(input())
p=input().split()
for i in input().split(): 
    a=0
    for j in range(len(p)):
        if int(i)%int(p[j])!=0 : a=1 
        break
    print("T" if a==0 else "F",end="")

input(),input()
p=list(map(int,input().split()));a=""
for i in input().split():
    x=int(i)
    for j in p:
        if x%j:a+='F';break
    else:a+='T'
print(a)

u=input()
print([["ftp://"+u,"http://"+u]["."in u],u][":"in u])

s = [str(x) for x in input().split()]
a1=[]
a2=[]
for i in s:
    if int(i)%2!=0:
        a1.append(str(i))
    else:
        a2.append(str(i))    
a1.sort()        
print(" ".join(a1),end=" ")
a2.sort(reverse=True)
print(" ".join(a2))

n = int(input())
count=0
for i in range(n):
    count1,count2,count3,count4,count5=0,0,0,0,0
    k = input()
    for s in k:
        count1= 1 if s=='P' else -1 if s=='p' else 0
        count2= 3 if s=='N' else -3 if s=='n' else 0
        count3= 3 if s=='B' else -3 if s=='b' else 0
        count4= 5 if s=='R' else -5 if s=='r' else 0
        count5= 9 if s=='Q' else -9 if s=='q' else 0
        count=count+count1+count2+count3+count4+count5
if(count!=0):
    print(count)
else:
    print('equal')

arr=[]
a=0
text = input()
arr.append(text[0])
for i in range(1,len(text)):
    if text[i].isalpha():
        if(ord(text[i])+i)>=122:
            a=ord(text[i])+i-122+97-1
        else: 
            a=ord(text[i])+i
        arr.append(chr(a))
    else:
        arr.append(text[i])
print("".join(arr))

m=input()
c='----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.'.split()
r=[]
try:
 for i in m:r+=[c[int(i)]]
except:r=[]
print(*r if len(r)==10 else["Untransformable"])

s = input()
r = input()
i=0
while i < len(s):
    try:
        j=s.index(r,i)+len(r)
        if i!=0:
            i-=len(r)
        print(s[i:j])
        i=j
    except ValueError:
        print(s[i-len(r):])
        break

a=[]
m=input()
for i in range(len(m)):
    if m[i].isalpha():
        a.append(str(i))
i=0
j=0
while i<len(m):
    if m[i].isalpha():
        print(m[int(a[j])].upper() if j%2==0 else m[int(a[j])].lower(),end="")
        j+=1
    else:
        print(m[i],end="")
    i+=1

n, m = [int(i) for i in input().split()]
s=n*m
if m==n: print(1)
else:
    count=0
    for i in range(1,int(s**0.5)):
        count=i
        if (round(s/i)**0.5)==int((s/i)**0.5):
            break
    print(i)

arr=[]
n = int(input())
for i in range(n):
    count=-1
    name = input()
    for i in range(len(name)):      
        if name[i]==",":
            arr.append(name[i+2:len(name)])
            continue
        else:
            count+=1
        if count==len(name)-1:
            arr.append("N/A")
print("\n".join(arr))

s = input().split()
print(s[len(s)//2-1]+s[len(s)//2] if len(s)%2==0 else s[(len(s)+1)//2-1])

n = int(input())
count=0
arr=[]
a1=""
arr=[i for i in input().split()]
while count<n:
    for i in range(n):
        if int(arr[i])==n-count:
            print("***",end=" ")
        elif int(arr[i])>=n-count: 
                print("* *",end=" ")
        else: print("   ",end=" ")
    count+=1
    print()
'''
i=["name",3000,3,41,5]
i[1:5].sort()
print(i)
print(i[1],i[2],i[3])