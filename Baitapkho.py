'''
#Bai1
#import re
arr=[]
pw=[str(x) for x in input("Input str password: ").split(',')]
for s in pw:
    count={'1':0,'2':0,'3':0,'4':0}
    length=len(s)
    if(6>length or length>12):
        continue
    else:
        for i in range(length):
            if('a'<=s[i] and s[i]<='z'): #re.search("[a-z]',p)
                count['1']+=1
            elif('0'<=s[i] and s[i]<='9'):
                count['2']+=1
            elif('A'<=s[i] and s[i]<='Z'):
                count['3']+=1
            elif(s[i]=='$' or s[i]=='#' or s[i]=='@'):
                count['4']+=1
            else:
                continue
        if(count['1']!=0 and count['2']!=0 and count['3']!=0 and count['4']!=0):
            arr.append(s)
print("Result: ")
if(arr==[]):
    print("Invalid output")
else: 
    print(','.join(arr))

#Bài 2
from operator import itemgetter, attrgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))
print (sorted(l, key=itemgetter(0,1,2)))

def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in putNumbers (100):
    print (i)
'''
# freq = {} # frequency of words in text
# line = input()
# for word in line.split():
#     freq[word] = freq.get(word,0)+1

# words = sorted(freq.keys())
# for w in words:
#     print ("%s:%d" % (w,freq[w]))

arr=[]
arr1=[i for i in input().split()]
for i in arr1:
    if i not in arr:arr.append(i)
arr.sort()
for i in arr:print(f"{i}:{arr1.count(i)}")