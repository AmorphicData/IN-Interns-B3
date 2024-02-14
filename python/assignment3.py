#Q1 - Built-in functions

#1.
l = [1, 2, 3, 4, 5]
print(len(l))  
#2
print(max(l))
#3
print(min(l))
#4
print(sum(l))
#5
l2=[3, 1, 4, 1, 5, 9, 2]
print(sorted(l2))
#6
print(round(3.14159, 2)) #Returns the floating-point number rounded to the specified number of decimals
#7
l3 = [0, False, None, 1]
print(any(l3)) #Returns True if any element of the iterable is true
#8
l4 = [1, True, "hello"] 
print(all(l4))  #Returns True if all elements of the iterable are true
#9
l5=["apple", "banana", "mango"]
for index, value in enumerate(l5): #Returns an enumerate object that yields pairs of indexes and corresponding values.
    print(index, value)
#10
l7 = [1, 2, 3, 4, 5]
my_slice = slice(2) #Returns a slice object representing the set of indices specified by range(start, stop, step)
print(l7[my_slice]) 
#11
name = "Kastubh"
age = 21
print("My name is {} and I am {} years old.".format(name, age)) #Returns a formatted representation of a value
#12
result = eval("2 + 3 * 4") #Evaluates a Python expression given as a string and returns the result
print(result)
#13
exec("x = 5\ny = 10\nprint(x + y)") #Executes Python code dynamically
#14
print(isinstance(5, int)) #Returns True if the object argument is an instance of the classinfo argument
#15
print(hash("hello")) #Returns the hash value of an object
#16
print(chr(65)) #Returns the string representing a character whose Unicode code point is the integer
#17
print(ord('A')) #Returns the Unicode code point for a one-character string
#18
print(type(5)) #Returns the type of an object
#19
print(bool(0)) #Converts a value to a Boolean
#20
def my_func():
    return True
print(callable(my_func))  # Returns True if the object appears callable
#21
l6 = [1, 2, 3]
print(id(l6))  #Returns the identity of an object
#22
print(bin(10)) #Converts an integer to a binary string 
#23
print(hex(255)) #Converts an integer to a hexadecimal string
#24
print(oct(8)) #Converts an integer to an octal string
#25
print(pow(2, 3)) 
#26
print(abs(-5))


#Q2 - Custom functions

# 1. max

l=[7,8,1,2,3,4,5]
maxx=l[0]
i=1
for i in l:
    if i>maxx:
        maxx=i
print (maxx)

#2. min

l=[7,8,1,2,3,4,5]
minn=l[0]
i=1
for i in l:
    if i<minn:
        minn=i
print (minn)
        
#3. len
        
l=[7,8,1,2,3,4,5]
c=0
for i in l:
    c=c+1
print (c)

#4. upper & 5. lower

l=['a','b','c','D','E','f']

result = ""
for char in l:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32) + " "
    elif 'a' <=char <= 'z':
        result += chr(ord(char) - 32) + " "
print(result)

#6. abs

x=int(input("Enter the Number: "))
if x>0:
    print (-x)
else:
    print(x)

#7. reverse
    
l=[7,8,1,2,3,4,5]
x=l[::-1]
print (x)

#8. count

x=int(input("Enter number of elements: "))
l=[]
for i in range(x):
    l.append(input())
print (l)
key=input("Enter key value to search in list: ")
for i in l:
    count = 0
    for element in l:
        if element == key:
            count += 1
print (count)
        
#9. avg

l=[7,8,1,2,3,4,5]

count=0
avg=0
for i in l:
    count +=1
print (count)
sum=0
for i in l:
    sum=sum+i
    avg=sum/count 
print (avg)
        
#10. sum
        
l=[7,8,1,2,3,4,5]
sum=0
for i in l:
    sum+=i
print(sum)
        
#11. sort
        
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
for i in range(n):
    # Last i elements are already in place
    for j in range(0, n-i-1):
        # Traverse the list from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted array:", arr)

#12. power
        
x=int(input())
y=int(input())
print(x**y)
        
