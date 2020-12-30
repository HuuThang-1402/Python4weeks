'''
# Cac ham toan hoc
import math
#from math import *
#radians(goc)
x=25 
print(math.sqrt(x))
print(math.pow(x,2))
print(math.log(x))
print(math.log10(100))

#Ham time time 
import time
print("Enter your name: ",end="")
start_time=time.time()
name=input()
elapsed=time.time()-start_time
print(name,"it took you", elapsed, "seconds to respond")
# for x in range (-10,10):
#     print(x)
#     time.sleep(1)

#Ham random
from random import randrange
count=0
while count<10:
    x=randrange(-100,100)
    if(count==9):
        print(x)
        
    else:
        print(x,end=",")
    count+=1
print("Bye!")

# exit() la thoat luon phan mem
# eval() tinh toan nhieu phep toan
# x1,x2 = eval(input("Nhap 2 so x1,x2: "))

#Game đoán số
from random import randrange
b=True
while b:
    count=0
    x=randrange(1,101)
    while count<7:
        a=int(input("Enter a number in [1,100] ({0}): ".format(count+1)))
        
        if (a<1 or a>100):
            print("Please re-enter a number in [1,100] (do not count this turn) ")
        else:
            if a<x:
                print("The number you enter is smaller than the number you need to find!")
                count+=1
            elif a>x:
                print("The number you enter is greater than the number you need to find!")
                count+=1
            else:
                print("That's right! You are so intelligent")
                print("The number to look for is:",x)
                break
    else:
        print("Game over! You are so stupid!")
        print("The number to look for is:",x)
    op='a'
    while op!='y' and op!='n':
        op=str(input("Do you want to continue(y/n): "))
    if(op=='y'):
        continue
    elif(op=='n'):
        print("Thank you for playing my game!")
        break

#Tính diện tích tam giác
from math import sqrt
bo=True
while bo:
    a,b,c=eval(input("Enter a,b,c: "))
    if (a+b)>c and (a+c)>b and (b+c)>a and (a>0) and (b>0) and (c>0):
        p=(a+b+c)/2
        dt=sqrt(p*(p-a)*(p-b)*(p-c))
        print("the area of the triangle (a,b,c) is:",dt)
        bo=False
    else:
        print("Invalid input! Please re-enter the input")
print("Thank you for using the software!")

#Vẽ hình
for i in range(7):
    for j in range(7):
        if (i<4 and j>=3 and j<=i+3) or (i>2 and j<=3 and i<=6-j):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
'''