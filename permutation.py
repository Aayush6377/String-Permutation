import random
import math
st=str(input("Enter string:"))
li=[]
for x in st:
    li.append(x)

c=0
for i in li:
    if li.count(i)!=1:
        c+=1
v=[]
for i in li:
    if li.count(i)!=1 and i not in v:
        v.append(i)
de=1
for g in v:
    de*=math.factorial(li.count(g))
per=math.factorial(len(li))/de

bi=[]
while len(bi)<per:
    b=''
    for i in range(len(li)):
            a=random.randint(0,len(li)-1)
            b+=li[a]
                
            ba=0
            for i in li:
                if i in b:
                    ba+=1
            t=0
            for x in li:
                if b.count(x)==li.count(x):
                    t+=1
                
    if b not in bi and len(b)==len(li) and t==len(li) and ba==len(li):
            bi.append(b)

bi.sort()
print('Number of permutations:',len(bi))
print(bi)
    
