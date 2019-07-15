str11=str(input())
lst=""
rev=str11
flag=0
for i in range(1,len(str11)):
    lst=str11[i:]
    if(lst[0]>str11[0]):
        rev=lst
        f=1
        break
print(rev) 
