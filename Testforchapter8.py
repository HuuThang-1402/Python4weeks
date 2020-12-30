'''
#insert: 
lst=[1,2,3]
lst.insert(2,9)
print(lst)
lst.insert(0,17)
print(lst)

a=int(input())
x=a-3
y=0
if a<3:y=3-a
for i in range(a):print(" "*(i+y)+"\\")
for e in [" _oO^____",
          "(._,     \\",
          "   \\  _\\ /\\",
          "    || ||",
          "~~~~~~~~~~~~~"]:
    print(" "*x+e)

words = input()
s=words.split()
a=len(s[0])
b=len(s[1])
a1=[]
a2=[]
for n in s[0]:
    a1.append(n.upper())
for n in s[1]:
    a2.append(n.upper())
for i in range(len(s[1])):
    for j in range(len(s[0])):
        if s[1][i]==s[0][j]:
            if a>=b:
                for m in range((len(s[1]))):
                    if m==i:
                        print(" ".join(a1))
                    else:
                        print(" "*j*2+s[1][m].upper())
            else:
                for m in range((len(s[0]))):
                    if m==j:
                        print(" ".join(a2))
                    else:
                        print(" "*i*2+s[0][m].upper())
            exit()
else: 
    print("NO COMMON CHARACTER")
         
lst=[0,1,2,3,4,5,1,10,11,1,4]
for i in lst:
    if i==1:
        lst.remove(1)
print(lst)
del lst[0]
print(lst)

lst=[0,1,2,3,4,5,1,10,11,1,4]
lst.reverse()
print(lst)
lst2=reversed(lst)
for i in lst2:
    print(i,end=" ")
print()
print(lst)

n=input().split()
a=0
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        a=i
        break
if a!=0: del n[a]
for i in (0,1):
    if abs(int(n[i+3])-int(n[i+2]))==1 and abs(int(n[i+2])-int(n[i+1]))==1 and abs(int(n[i+1])-int(n[i]))==1:
        print("true")
        break
else: print("false")
s=sorted(set(map(int,input().split())))
L=len(s)
print(str((L==4 and s[3]-s[0]==3)or(L==5 and (s[3]-s[0]==3 or s[4]-s[1]==3))).lower())

#Bai2
from random import randrange
n=int(input("Nhập 1 số n: "))
arr=[0]*n
for i in range(n):
    arr[i]=randrange(0,51)
print(arr)
k=int(input("Enter a number which you want delete: "))
while arr.count(k)>0:
    arr.remove(k)
print(arr)
a1=str(input("Enter a string: "))
for i in range(len(a1)//2):
    if a1[i]!=a1[len(a1)-1-i]:
        print("This string is asymmetric")
        break
else: print("This string is symmetrical")

#Bai 3
from random import randrange
m=int(input("Enter the value of m: "))
n=int(input("Enter the value of n: "))
arr=[[0 for _ in range(n)] for _ in range(m)]
max=0
for i in range(m):
    for j in range(n):
        arr[i][j]=randrange(0,100)
        if arr[i][j]>max:
            max=arr[i][j]
for i in range(m):
    for j in range(n):
        print(arr[i][j],end="\t")
    print()
print(arr[randrange(0,m)])
a=randrange(0,m)
for i in range(m):
    print(arr[i][a])
print(max)

#Cau 3:
from random import randrange
n=int(input("Enter a number: "))
arr=[]
for i in range(n):
    op=True
    while op:
        a=randrange(101)
        if str(a) not in arr:
            arr.append(str(a))
            op=False
print(" ".join(arr))

#Cau 4
arr=[]
arr1=[]
i=0
while True:
    s=input()
    if not s:
        break
    if i==0:
        arr.append(int(s))
        arr1=sorted(arr)
    else:
        if int(s)<arr1[len(arr)-1]:
            print("You entered incorrectly, Please re-enter a number:")
            s=input()
        arr.append(int(s))
        arr1=sorted(arr)
    i+=1
print("Your string is:",arr)

n=int(input("Enter a number: "))
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
print(arr)
print(sorted(arr,reverse=True))

def isPrime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0: count+=1
    return count==2
def main():
    from random import randrange
    arr=[]
    n=int(input("Enter a number: "))
    for i in range(n):
        arr.append(randrange(20))
    print(arr)
    arr1=[]
    for i in arr:
        if i%2==1 and i not in arr1:
            print(i if arr.count(i)==1 else "{0}({1})".format(i,arr.count(i)),end=" ")
            arr1.append(i)
    print()
    arr2=[]
    for i in arr:
        if i%2==0 and i not in arr2:
            print(i if arr.count(i)==1 else "{0}({1})".format(i,arr.count(i)),end=" ")
            arr2.append(i)
    print()
    arr3=[]
    for i in arr:
        if isPrime(i) and i not in arr3:
            print(i if arr.count(i)==1 else "{0}({1})".format(i,arr.count(i)),end=" ")
            arr3.append(i)
    print()
    arr4=[]
    for i in arr:
        if isPrime(i)==False and i not in arr4:
            print(i if arr.count(i)==1 else "{0}({1})".format(i,arr.count(i)),end=" ")
            arr4.append(i)
    print()
main()

max=0
words = input()
for i in words:
    if i!=" ":
        if max<words.count(i):
            max=words.count(i)
            print(i)
print(max)
a=256
w=sum(map(ord,input()))%a
print(f"{w}.{2*w%a}.{3*w%a}.{4*w%a}")
'''




    

