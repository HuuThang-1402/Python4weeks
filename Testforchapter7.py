'''
word="Nguyễn Hữu Thắng"
print(word.rjust(30))
print(word.rjust(30,"*")) # Căn lề phải
print(word.ljust(30))
print(word.ljust(30,"*")) # Căn lề trái
print(word.center(30))
print(word.center(30,"*")) # Căn giữa

s="## Thang###"
print(s.strip("#")) #Loại bỏ phía đầu và cuối ký tự trong ngoặc 
'''
s="*Hello World#"
print(s.startswith("#"))
print(s.startswith("*"))
print(s.endswith("#"))
print(s.endswith("*"))
'''
s="Nguyen Huu Thang, Vo Thi Lan Anh, anh em"
print(s.find("n"))
print(s.rfind("n"))
print(s.find("x"))
print(s.count("Anh"))
print(s.count("ngu"))

s="C:/HocTap/Python/Testforchapter7.py"
print(s[:3])
print(s[3:])
print(s[-5:])
print(s[:-5])
print(s[5:-10])
print(s[10:15])
print("*"*15)
print(s[5:]+s[:5])
print(s[-5:]+s[:-5])

#Bài xuất chuỗi đối xưng
op=True
while op:
    s=str(input("Nhập 1 chuỗi bất kì: "))
    for i in  range(len(s)//2):
        if s[i]!=s[len(s)-1-i]:
            print("Chuỗi {0} không đối xứng".format(s))
            break
    else: print("Chuỗi {0} đối xứng".format(s))
    op1="a"
    while op1!='y' and op1!="n":
        op1=str(input("Bạn có muốn tiếp tục không (y/n): "))
    op=True if op1=='y' else False
print("Thanks for using this software!!!")

#Bai tap toi uu chuoi
def Toiuu(s):
    s=s.strip()
    s=s.split()
    arr=[]
    for i in s:
        if i.strip()!="":
            arr.append(i)
    print(" ".join(arr))
    print(len(" ".join(arr)))
def main():
    s=str(input("Enter a string: "))
    Toiuu(s)
main()

#Bai3
def Chusochan(s):
    for i in s:
        if int(i)>0:
            if int(i)%2==0:
                print(i,end=" ")
def soam(s):
    count=0
    for i in s:
        if int(i)<0:
            count+=1
    print(count)
def isprime(i):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    return count==2
def tb(s):
    a=0
    for i in s:
        a+=int(i)
    print(round(a/len(s),2))
def main():
    s="5;7;8;-2;8;11;13;9;10"
    s=s.split(";")
    print("Cau a:")
    for i in s:
        print(i)
    print()
    print("*"*15)
    print("cau b:")
    Chusochan(s)
    print()
    print("*"*15)
    print("cau c:")
    soam(s)
    print()
    print("*"*15)
    print("cau d:")
    for i in s:
        if isprime(int(i))==True:
            print(i,end=" ")
    print()
    print("*"*15)
    print("cau e:")
    tb(s)
main()

#Cau 2
count1,count2,count3,count4,count5,count6,count7=0,0,0,0,0,0,0
s=str(input("Enter a string: "))
for i in s:
    if i.isupper():count1+=1
    elif i.islower():count2+=1
    elif i.isdigit():count3+=1
    elif i==" ":count5+=1
    else : count4+=1
    if i.isalpha():
        i=i.lower()
        if i in ('a','o','i','u','e'): count6+=1
        else :count7+=1
print("Số chữ in hoa là:",count1)
print("Số chữ in thường là:",count2)
print("Số chữ số là:",count3)
print("Số ký tự đặc biệt là:",count4)
print("Số khoảng trắng là:",count5)
print("Số nguyên âm là:",count6)
print("Số phụ âm là:",count7)

#Cau3
def NegativeNumberInString(s):
    count=0
    i=0
    a1=[]
    while i<len(s)-1:
        if s[i]=="-" and s[i+1].isdigit():
            arr="-"
            for j in range(i+1,len(s)):
                if s[j].isdigit():
                    arr+=s[j]
                    i=j
                else: break
            count+=1
            a1.append(arr)
        i+=1
    print("Các số âm là:",end=" ")
    print(",".join(a1))
    print("Tổng số âm là:",count)
def main():
    op1=True
    while op1:
        s=str(input("Enter a string:"))
        NegativeNumberInString(s)
        op='a'
        while op!='y' and op!='n':
            op=str(input("Do you want to continue (y/n):"))
        if op=='y':op1=True
        else:op1=False
    print('Thanks for using this software!!')
main()

#Cau4
def Toiuuchuoi(s):
    s=s.strip()
    s=s.split()
    arr=[]
    for i in s:
        if i.strip()!="":
            b=""
            for j in range(len(i)):
                if j==0: b+=i[j].upper()
                else: b+=i[j].lower()
            arr.append(b)
    print(" ".join(arr))
def main():
    s=str(input("Enter a string:"))
    Toiuuchuoi(s)
main()
'''

    