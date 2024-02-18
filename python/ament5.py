from functools import reduce
# Q-1
'''li=[1,2,3,4,5,6,7,8]
def iodd(n):
    if(n%2):
        return True
    
def sq(n):
    return n*n'''
#r=list(map(sq,list(filter(iodd,li))))
#r=list(map(lambda n:n*n,list(filter(iodd,li))))
#print(r)
# Q-2
'''li=[1,2,3,5]
def fac(n):
    if(n==0):
        return 1
    return n*(fac(n-1))
r=list(map(fac,li))
print(r)'''
#Q-3
'''li=['Rohan','Dev','Raj']
li2=[10,9,11]
r=list(zip(li,li2))
di={}
def cre(t):
     di[t[0]]=t[1]
for i in r:
     cre(i) 
print(di)'''
#q-4
'''li=[5,6,7,10]
li2=[10,9,4,78]
ir=list(zip(li,li2))
def fil(n1):
    if(n1[0]>n1[1]):
        return 1
    
    
def fil1(n1):
    if(n1[0]>n1[1]):
        return n1[0]
    return n1[1]
r=list(filter(fil,ir))
r1=list(map(fil1,ir))

print(r)
#[(7, 4)]
print(r1)
#[10, 9, 7, 78]
'''
#Q-5

#Q-6
'''ts1=input().split(',')
ts2=input().split(',')
ts3=input().split(',')
li=list(zip(ts1,ts2,ts3))
def fun(t):
    if((int(t[0])<int(t[1])+int(t[2]))&(int(t[1])<int(t[2])+int(t[0]))&(int(t[2])<int(t[1])+int(t[0]))):
       return 1
    return 0
    
r=list(filter(fun,li))
print(r)'''

#Q-7
'''li=['aei','bdc','aabc','uuu']
lv=['a','e','i','o','u']
def isv(s):
    for i in s:
        if(i not in lv):
            return 0
        
    return 1
def fil(e):
    if(isv(e)):
        return 0
    return 1
ir=list(filter(fil,li))
fs=reduce(lambda x,y:x+","+y,ir)
print(fs)'''
    
#Q-8
'''def read_large_file(sample):
    try:
        with open(sample, 'r') as file:
            for line in file:
                yield line.strip('\n')
    except FileNotFoundError:
        pass

gen=read_large_file("sample.txt")
print(next(gen))'''
#Q-9
'''def fun():
    
    
    count=0
    a=0
    b=1
    while(True):
        if count==0:
            yield 0
        if count==1:
            yield 1
        else:
           c=a+b
           yield c
           a=b
           b=c
        count+=1'''
'''def fun(n):
    di={}
    fi=2
    count=0
    while(count<n):
        if(di.get(fi,0)==False):
           yield fi
           j=2
           while(j*fi<=n):
               di[j*fi]=1
               j+=1
        fi+=1
        count+=1
               
gen=fun(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))'''
#MAP
'''def fun(n1):
    return n1*n1
def map(n1,n2):
    for i in range(0,len(n2)):
        n2[i]=n1(n2[i])
    return n2
l=[1,2,4]
print(map(fun,l))'''
#FILTER
'''def fun(n1):
    if(n1>0):
        return True
    return False
def filter(n1,n2):
    re=[]
    for i in n2:
        if(n1(i)):
            re.append(i)
    return re
l=[-1,-2,4]
r=filter(fun,l)
print(r)'''
#ZIP
'''def zip(*args):
    r=[]
    m=(10**9)
    totals=len(args)
    for i in args:
        m=min(len(i),m)
    c=0
    while(c<m):
        et=()
        j=0
        while(j<totals):
            
            ti=()+(args[j][c],)    
            net=et+ti
            et=net
            j+=1
        
        r.append(et)
        c+=1
    return r

l1=[1,2,3]
l2=[2,3,4]
l3=[1,2]
r=zip(l1,l2,l3)
print(r)'''
#REDUCE
'''def fun(n1,n2):
    return n1*n2
def reduc(n1,n2,n3=0):
    s=n3
    for i in range(0,len(n2)):
       s=n1(s,n2[i])
    return s
l=[1,2,4]
print(reduce(fun,l,1))'''
    

        


        









