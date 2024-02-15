import sys
#Length Function
def lenm(l):
        count=0
        for i in l:
                count=count+1
        return count
'''#Max Func
def max(l):
        mx=-sys.maxsize -1
        for i in l:
                if(i>mx):
                        mx=i
        return mx
#Min Func
def min(l):
        mn=sys.maxsize
        for i in l:
                if(i<mn):
                        mn=i
        return mn

# uppper
def upper(s):
    c=0
    r=''
   #print(lenm(s))
    while c <lenm(s):
       # print(1)
        if('A'<=s[c]<='Z'):
               r+=s[c]
               c=c+1
               
               continue
        else:
               r+=chr(ord(s[c])-ord('a')+ord('A'))
        c=c+1
    return r
print(upper('AbD')) '''  
#Range Func
def ranges(*args):
        l=[]
        st=0
        end=0
        step=1
        if(lenm(args)>3):
              return 0
        if(lenm(args)==1):
                end=args[0]
        elif(lenm(args)==2):
                st=args[0]
                end=args[1]
                if(end<st):
                 end=st  
        else:
                st=args[0]
                end=args[1]
                step=args[2]
                if(end<st):
                 end=st  
        while(st<end):
         l.append(st)
         st=st+step
        return l

'''l=[1,2,4,5,6]
for i in ranges(0,lenm(l),2):
      print(l[i])'''

def sqrt(n):
      if(n==1|n==0):
            return n
      for i in ranges(1,n):
            if(i*i>n):
                return i-1
def abs(n):
      if(n>0):
            return n
      n=n*(-1)
      return n
def pow(b,p):
      if(p==0):
            return 1
      return p*pow(b,p-1)
n=int(input())
print(abs(n))
def sum(l):
      sum=0
      for i in l:
            sum=sum+i
      return sum
def avg(l):
      sum=0
      for i in l:
            sum=sum+i
      lent=lenm(l)
      return sum/l
l = [1, 2, 3, 4, 5]
print(len(l))  
print(max(l))
print(min(l))
print(sum(l))
l2=[3, 1, 4, 1, 5, 9, 2]
print(sorted(l2))
print(round(4.78159, 2)) 
l3 = [0, False, None, 1]
print(any(l3)) 
l4 = [1, True, "hello"] 
print(all(l4))  
l5=["apple", "banana", "mango"]
for index, value in enumerate(l5): 
    print(index, value)

l7 = [1, 2, 3, 4, 5]
l = slice(2) 
print(l7[l]) 

name = "Saksham"
age = 21
print("My name is {} and I am {} years old.".format(name, age)) 

result = eval("5 * 3 * 4") 
print(result)

exec("x = 6\ny = 12\nprint(x * y)") 

print(isinstance(5, int)) 

print(hash("hello")) 

print(chr(65)) 

print(ord('A')) 

def my_func():
    return True
print(callable(my_func))  # Returns True if the object appears callable

li = [1, 2, 3]
print(id(li))  

print(bin(10))  

print(hex(255)) 

print(oct(8)) 

print(pow(2, 3)) 

print(abs(-5))


print(type(5)) 

print(bool(0)) 

     
            
