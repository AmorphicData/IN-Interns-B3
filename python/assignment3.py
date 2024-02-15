#maximum funtion Implementation
L=[1,42,3,4,7] #java vaale array idhar voh list hoti hai
max_num=-1
for i in L:
   if i>max_num:
      max_num=i

print(max_num)

#minimum funtion Implementation
List_str=input("Enter a List of Numbers by space").split()
input_list = [int(i) for i in List_str] #List Comphresion convert karne ke Kaam aate hai
print(input_list)
min_num=10**9
for i in input_list:
   if i<min_num:
      min_num=i
print(min_num)

#Length without using len function
List=input("Enter the numbers with space").split()
input_list=[int(i) for i in List]
count=0
for i in range(len(input_list)):
   count=count+1
print(count)

#without range
List=input("Enter the numbers with space").split()
input_list=[int(i) for i in List]
count=0
for i in input_list:
   count=count+1
print(count)


#Sort
def length(L):
   count=0
   for i in L:
      count+=1
   return count

List=input("Enter the numbers with space").split()
input_list=[int(i) for i in List]
n=length(input_list)
for i in range(n):
   for j in range(0,n-i-1):
      if input_list[j]>input_list[j+1]:
        input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
print(input_list)


#Range Without inbuilt function
def custom_range(start,stop=None,step=1):
   #agar stop nahi de rakha hai toh start hi stop hoga
   if stop==None:
      stop=start
      start=0
   
   ans=[]
   if step>0:
      #badti hue range hai
      while start<stop:
         ans.append(start)
         start+=step
   elif step<0:
      #decrease vaali range
     while start>stop:
            ans.append(start)
            start += step
    
   return ans


print(custom_range(5))
print(custom_range(1,5))
print(custom_range(1,5,2))

#sum
List=input("Enter the numbers with space").split()
input_list=[int(i) for i in List]
sum=0
for i in input_list:
    sum+=i
print(sum)

#average
List=input("Enter the numbers with space").split()
input_list=[int(i) for i in List]
count=0
for i in input_list:
    count+=1
sum=0
for i in input_list:
    sum+=i
avg=sum/count
print(avg)

#abs
num=int(input("Enter a number"))
print(num)
if  num<0:
    print (num)
else:
    print(-num)

#power function
def custom_power(base,exponent):
    if exponent==0:
        return 1
    elif exponent==1:
        return base
    else:
        return base*custom_power(base,exponent-1)
    
print(custom_power(2,3))

#reverse function
List=input("Enter the numbers with space").split()
input_list=[int(i) for i in List]
print(input_list[::-1])



##################BUILT FUNCTIONS###############

#1)Combines multiple iterables into tuples of corresponding elements.
list1=[1,2,3]
list2=['a','b','c']
zipped=zip(list1,list2)
print(list(zipped))

#2)enumerate(): Returns an enumerate object that yields pairs of indices and corresponding values from an iterable.
for i,item in enumerate(['a','b','c']):
    print(i,item)

#3)any():Returns true if atleast one condition is true
print(any([False,True,False]))

#4)all():Returns True all are True
print(all([True,True,True]))

#5)Filter():filter elements from iterable based on function
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]

#6)map():applies function to every item that is iterable
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#7)sort():it will sort the array
nums=[2,3,4,1]
print(sorted(nums))

#8)round():Rounds a number to a specified number of decimals (defaults to 0).
num=3.14256
print(round(nums))

#9)chr(): Returns the string representing a character whose Unicode code point is the integer.
print(chr(97))

#10)ord(): Returns the Unicode code point for a one-character string.
print(ord('a'))

#11)abs():Returns the absolute value
print(abs(-5))

#12)id():Returns the identity of object 
l1=[1,2,3,4]
print(id(l1))

#13)oct():convert an Integer into octal String
print(oct(8))

#14)hex():convert the Integer into hexadecimal String
print(hex(255))

#15)bin():convert Integer into Binary
print(bin(10))

#16)hash():Returns the Hash value of an object
print(hash("Rounak"))

#17)format():#Returns a formatted representation of a value
name = "Rounak"
age = 21
print("My name is {} and I am {} years old.".format(name, age)) 

#18)pow():Returns output as power function
print(pow(2,3))

L1=[1,2,3,4,5,6]
#19)max():will return max value among list
print(max(L1))

#20)min():print min value among list
print(min(L1))

#21)len():Print len of the list
print(len(L1))

#22)sum():Return sum of the List
print(sum(L1))

#23)bool():Converts the value to bool
print(bool(0))

#24)locals(): Returns a dictionary representing the current local symbol table.
def my_func():
    x = 10
    print(locals())

my_func()
# Output: {'x': 10}

#25)getattr(): Returns the value of the named attribute of an object.
class MyClass:
    x = 10

obj = MyClass()
print(getattr(obj, 'x'))  # Output: 10
