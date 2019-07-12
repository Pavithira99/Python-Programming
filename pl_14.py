ans=int(input())
ver=list(map(str,input()[:ans]))
vow=['a','e','i','o','u','A','E','I','O','U']
rq=[]
for i in ver:
   if i not in vow:
      rq.append(i)
print(''.join(map(str,rqr[::-1]))) 
