'''
n = int(input())
a=hex(n).split('x')[-1][-1:]
n*=a
n=int(n,16)
print(bin(int(n))[-1:])

a, n = [int(i) for i in input().split()]
for i in range(n):
    c=""
    b=bin(a)[2:]
    x=int(input())
    for j in range(len(b)):
        if x==j: c+="1" if b[j]=="0" else "0"
        else: c+=b[j]
    print("c=",c)
    a=int(c,2)
print(a)


x=0
arr=[]
a1,a2=[],[]
n = int(input())
for i in range(n):
    a=input().split()
    if a[1]=="+":
        x=int(a[0])+1
        a1.append(int(a[0]))
        if a2!=[]:
            if int(a[0])>max(a2):print("Impossible");exit()
    elif a[1]=="-":
        x=int(a[0])-1
        a2.append(int(a[0]))
        if a1!=[]:
            if int(a[0])<max(a1):print("Impossible");exit()
    else:x=int(a[0])
    arr.append(x)
for i in arr:
    if n==1: 
        if 0<=arr[0]<=100: print(arr[0]);exit()
    else:
        if arr.count(i)>=2:
            if 0<=n<=100:print(i);exit()
else: print("Impossible")

n = int(input())
arr = input().split()
d, pos = input().split()
pos = int(pos)%len(arr)
if d=='Left':print(*arr[pos:],*arr[:pos])
else:print(*arr[-pos:],*arr[:-pos])

n=int(input())
m=input()
m+="x"*(n>1)*(n-len(m)%n)
print(*[m[i:len(m):n]for i in range(n)])

n=int(input())
a="#"*n
print(a)
arr=[]
for i in range(1,n-1):
    b=""
    if i<=(n-1)//2:
        for j in range(n):
            if j<i or j>=n-i:print(a[j],end="");b+=a[j]
            else: 
                if a[i]=="o":print("#",end="");b+="#"
                else: print("o",end="");b+="o"
        arr.append(b)
        a=b
        print()
    else: print(arr[n-1-i-1])
print("#"*n)

from collections import Counter as C
n = int(input())
print(C(list(map(int, input().split()))).most_common()[1][0])
'''
s=input()
a=""
i=0
while i<len(s):
    if s[i].isdigit():a=a+s[i]
    else:
        for j in range(i,len(s)):
            if s[j].isdigit() or j==len(s)-1:
                if j==len(s)-1:j=len(s)
                b=s[i:j]
                print(b*int(a),end="")
                a=""
                i=j-1
                break
    i+=1
