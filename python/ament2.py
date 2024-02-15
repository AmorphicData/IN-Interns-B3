import copy
'''a=int(input())
print('Positive and even')(ifa%2==0)('Positive and odd')if(a>0)print('negative and even')(ifa%2==0)('negative and odd')
a=int(input())
if(a>90):
    print('Grade is S')
elif(a>80):
    print('Grade is A')
elif(a>70):
    print('Grade is B')
elif(a>60):
    print('Grade is C')
else:
    print('Grade is F')




#a=int(input())
vl=['a','e','i','o','u']
cl=[]
for i in range(97,123):
    if(chr(i) in vl):
        continue
    else:
        cl.append(chr(i))
a=input()
if(a.lower() in vl):
    print('Vowel')
elif(a.lower() in cl):
    print('Consonant')
else:
    print('Special character')
a=int(input())
if(a<=3 & a>=1):
    print('Spring')
elif(a>3 & a<=6):
    print('Summer')
elif(a>7 & a<=9):
    print('Autumn')
else:
    print('Winter')
#Functions
def findmax(a,b,c):
    mx=a
    if(b>mx):
        mx=b
    if(c>mx):
        mx=c
    return mx

a=int(input())
b=int(input())
c=int(input())
print('Max of a,b,c: ',findmax(a,b,c))
def fac(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    return n*fac(n-1)
a=int(input())
print(fac(a))
#Function with arguments
def concat(*strs):
    result=' '.join(strs)
    return result
print(concat('Hello','world'))
def lengthofargs(*strs):
    
    return len(strs)
print(lengthofargs('Hello','world'))
def pname(**strs):
    l=[]
    l.append(strs['Name'])
    l.append(strs['LastName'])
    return ' '.join(l)
print(pname(Name='John',LastName='Smith'))
def createdict(**dictargs):
    d=dict({})
    for key,value in dictargs.items():
        d[key]=value
    return d
print(createdict(FirstName='John',LastName='Smith'))
def createtu(*targs):
   
    return targs
print(createtu('John','Smith'))
def defargs(n1,n2=5):
    print(n1," ",n2)
defargs(n2=1,n1=6)
#TRY and EXCEPTION
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    print(1)

divide_numbers(10, 2) 
divide_numbers(5, 0)
def invalid():
    try:
        a=int(input())
        print("valid")
    except ValueError:
        print('Invalid Input')
    print('Done')
invalid()
def out_of_range(lst, index):
    try:
        result = lst[index]
        return result
    except IndexError:
        print(f"Index {index} is out of range for the list.")
        
ls=[1,2,3,4,5]
out_of_range(ls,9)
def multiple(lst,a,b):
    try:
        val=lst[10]
        result=a/b
    except (ZeroDivisionError,ValueError,IndexError) as e:
        print('Error ',e)

lst=[1,2,3,4]
multiple(lst,5,0)
year=int(input())
month =int(input())
mon31=[1,3,5,7,8,10,12]
f=False
if(year%4==0):
    if(year%100 !=0):
        print('Leap Year')
        f=True
    else:
         if(year%400!=0):
             print('Non-Leap year')
         else:
             f=True
             print('Leap Year')
       
if(month in mon31):
    print(31)
elif(month==2):
    if(f):
        print(29)
    else:
        print(28)
else:
    print(30)
a=int(input())
(print('Positive and even')if(a%2==0)else('Positive and odd'))if(a>0)else(print('negative and even')if(a%2==0)else('negative and odd'))
b=[1,2,[1,2,3]]
a=copy.copy(b)
print(id(b))
print(id(a))
b.append(4)
print(a)
print(b)'''











