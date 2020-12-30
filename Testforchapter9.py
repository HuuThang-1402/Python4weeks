'''
def SaveFile(path):
    file=open(path,"w",encoding="utf-8")
    file.writelines("SV001;Nguyễn Hữu Thắng;25/10/2000\n")
    file.writelines("SV002;Nguyễn Trần Thùy Trang;24/02/2009\n")
    file.writelines("SV002;Nguyễn Trần Thùy Trang;24/02/2000\n")
    file.writelines("SV002;Phan Văn Hào;24/02/2009\n")
    file.close()
SaveFile("csdlsv.txt")

def ReadFile(path):
    file=open(path,'r',encoding="utf-8")
    for line in file:
        print(line.strip())
    file.close()
ReadFile("csdlsv.txt")
'''
from Xulifile import *
while True:
    code=input("Enter the product code: ")
    if not code:
        break
    name=input("Enter the product name: ")
    price=float(input("Enter the product price: ")) 
    data=code+";"+name+";"+str(price)
    SaveFile("database.txt",data)
dssp=ReadFile("database.txt")
for row in dssp:
    for i in row:
        if i==row[1]:
            print(i.ljust(len("cocacola")),end="\t")
        else: print(i,end="\t")
    print()
print("*"*20)
for i in range(len(dssp)):
    for j in range(len(dssp)):
        a=dssp[i]
        if dssp[i][2]<dssp[j][2]:
            dssp[i]=dssp[j]
            dssp[j]=a
for row in dssp:
    for i in row:
        if i==row[1]:
            print(i.ljust(len("cocacola")),end="\t")
        else: print(i,end="\t")
    print()

def ReadFile(path):
    a1=[]
    file=open(path,'r',encoding="utf-8")
    for i in file:
        i=i.strip("\n")
        a1.append(i.split(","))
    file.close()
    return a1
def main():
    data=ReadFile("data.txt")
    for row in data:
        for col in row:
            print(col,end=" ")
        print()
    print("*"*20)
    for row in data:
        for col in row:
            if int(col)<0:
                print(col,end="\t")
        print()
main()
'''
from random import randrange
def SaveFile(path,data):
    file=open(path,'a',encoding="utf-8")
    file.writelines(data)
    file.writelines("\n")
    file.close()
def ReadFile(path):
    arr=[]
    file=open(path,'r',encoding="utf-8")
    for i in file:
        i.strip()
        i.split(";")
        arr.append(i)
    file.close()
    return arr
def main():
    while True:
        data=input()
        if not data: break
        SaveFile("filetext.txt",data)       
    arr=ReadFile("filetext.txt")
    for i in arr:
        a=0
        for j in i:
            if j.isdigit():a+=int(j)
        print(a)
main()
'''




