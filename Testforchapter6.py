'''
def UCLN(a,b):
    """ Hàm này để tìm UCLN của a và b """
    min=a if a<b else b
    for i in range(min,0,-1):
        if a%i==0 and b%i==0:
            return i
print(UCLN(15,5))

#Bai
def sum1(n):
    s=0
    while n>0:
        s+=1
        n-=1
    return s
def sum2():
    s=0
    global val
    while val>0:
        s+=1
        val-=1
    return s
def sum3():
    s=0
    for i in range(val,0,-1):
        s+=1
    return s
def main():
    print("Câu c")
    global val
    val=5
    print(sum2())
    print(sum1(5))
    print(sum3())
main()
'''
