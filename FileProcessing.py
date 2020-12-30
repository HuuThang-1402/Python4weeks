path = "databaseGE.txt"
def SaveFile(line):
    file = open(path,'a',encoding='utf-8')
    file.writelines(line)
    file.writelines('\n')
    file.close()
def ReadFile():
    arrBook=[]
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data=line.strip()
        arr=data.split(";")
        arrBook.append(arr)
    file.close()
    return arrBook