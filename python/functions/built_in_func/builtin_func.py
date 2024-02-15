###abs
#  integer number     
integer = -20  
print('Absolute value of -20 is:', abs(integer))  
  
#  floating number  
floating = -20.83  
print('Absolute value of -20.83 is:', abs(floating))  

###all - true if all are true or empty
# all values true  
k = [1, 3, 4, 6]  
print(all(k))  
  
# all values false  
k = [0, False]  
print(all(k))  
  
# one false value  
k = [1, 3, 7, 0]  
print(all(k))  
  
# one true value  
k = [0, False, 5]  
print(all(k))  
  
# empty iterable  
k = []  
print(all(k))  

###any - true if any one is true
l = [4, 3, 2, 0]                              
print(any(l))                                   
  
l = [0, False]  
print(any(l))  
  
l = [0, False, 5]  
print(any(l))  
  
l = []  
print(any(l))  

###bin - binary representation of a specified integer
x =  10  
y =  bin(x)  
print (y)  


###bool - converts a value to boolean(True or False) using the standard truth testing procedure.
test1 = []  
print(test1,'is',bool(test1))  
test1 = [0]  
print(test1,'is',bool(test1))  
test1 = 0.0  
print(test1,'is',bool(test1))  
test1 = None  
print(test1,'is',bool(test1))  
test1 = True  
print(test1,'is',bool(test1))  
test1 = 'Easy string'  
print(test1,'is',bool(test1))  

###bytes - The python bytes() in Python is used for returning a bytes object. 
#It is an immutable version of the bytearray() function.
#immutable version of the bytearray() function

string = "Hello World."  
array = bytes(string, 'utf-8')  
print(array) 

###bytearray - returns a bytearray object and can convert objects into bytearray objects, or create an empty bytearray object of the specified size.

string = "Python is a programming language."  
  
# string with encoding 'utf-8'  
arr = bytearray(string, 'utf-8')  
print(arr)  

###Python callable() Function - This built-in function checks and returns true if the object passed appears to be callable, otherwise false.
x = 8  
print(callable(x))  

### Python compile() Function - It takes source code as input and returns a code object which can later be executed by exec() function.

code_str = 'x=5\ny=10\nprint("sum =",x+y)'  
code = compile(code_str, 'sum.py', 'exec')  
print(type(code))  

### Python exec() Function - dynamic execution of Python program which can either be a string or object code and it accepts large blocks of code
exec(code)  

###eval()
x = 8  
print(eval('x + 1'))  

# DIFF: eval() function only accepts a single expression unlike exec which accepts single/block of code.

###Python sum() Function
s = sum([1, 2,4 ])  
print(s)  
  
s = sum([1, 2, 4], 10)  
print(s) 

###Float func
# for integers  
print(float(9))  
  
# for floats  
print(float(8.19))  
  
# for string floats  
print(float("-24.27"))  
  
# for string floats with whitespaces  
print(float("     -17.19\n"))  
  
# string float error  
print(float("xyz")) 

###Format func
# d, f and b are a type  
  
# integer  
print(format(123, "d"))  
  
# float arguments  
print(format(123.4567898, "f"))  
  
# binary format  
print(format(12, "b"))  

###SETATTR
class Student:  
    id = 0  
    name = ""  
      
    def __init__(self, id, name):  
        self.id = id  
        self.name = name  
          
student = Student(102,"Sohan")  
print(student.id)  
print(student.name)  
#print(student.email) product error  
setattr(student, 'email','sohan@abc.com') # adding new attribute  
print(student.email)  

###GETATTR

class Details:  
    age = 22  
    name = "Phill"  
  
details = Details()  
print('The age is:', getattr(details, "age"))  
print('The age is:', details.age)

###Iter
# list of numbers  
list = [1,2,3,4,5]  
  
listIter = iter(list)  
  
# prints '1'  
print(next(listIter))  
  
# prints '2'  
print(next(listIter))  
  
# prints '3'  
print(next(listIter))  
  
# prints '4'  
print(next(listIter))  
  
# prints '5'  
print(next(listIter))

###Len
strA = 'Python'  
print(len(strA))  

###List
# empty list  
print(list())  
  
# string  
String = 'abcde'       
print(list(String))  
  
# tuple  
Tuple = (1,2,3,4,5)  
print(list(Tuple))  
# list  
List = [1,2,3,4,5]  
print(list(List))  

###MAP
def calculateAddition(n):  
  return n+n  
  
numbers = (1, 2, 3, 4)  
result = map(calculateAddition, numbers)  
print(result)  
  
# converting map object to set  
numbersAddition = set(result)  
print(numbersAddition)  

###ENUMERATE
# Calling function  
result = enumerate([1,2,3])  
# Displaying result  
print(result)  
print(list(result))  

###FILTER
# Python filter() function example  
def filterdata(x):  
    if x>5:  
        return x  
# Calling function  
result = filter(filterdata,(1,2,6))  
# Displaying result  
print(list(result))  


###isinstance
class Student:  
    id = 101  
    name = "John"  
    def __init__(self, id, name):  
        self.id=id  
        self.name=name  
  
student = Student(1010,"John")  
lst = [12,34,5,6,767]  
# Calling function   
print(isinstance(student, Student)) # isinstance of Student class  
print(isinstance(lst, Student))  

###RANGE
# empty range  
print(list(range(0)))  
  
# using the range(stop)  
print(list(range(4)))  
  
# using the range(start, stop)  
print(list(range(1,7 )))  

###REVERSED
# for string  
String = 'Java'  
print(list(reversed(String)))  
  
# for tuple  
Tuple = ('J', 'a', 'v', 'a')  
print(list(reversed(Tuple)))  
  
# for range  
Range = range(8, 12)  
print(list(reversed(Range)))  
  
# for list  
List = [1, 2, 7, 5]  
print(list(reversed(List)))  

###round
#  for integers  
print(round(10))  
  
#  for floating point  
print(round(10.8))  
  
#  even choice  
print(round(6.6))  


###TYPE
List = [4, 5]  
print(type(List))  
  
Dict = {4: 'four', 5: 'five'}  
print(type(Dict))  
  
class Python:  
    a = 0  
  
InstanceOfPython = Python()  
print(type(InstanceOfPython))  

###ZIP
numList = [4,5, 6]  
strList = ['four', 'five', 'six']  
  
# No iterables are passed  
result = zip()  
  
# Converting itertor to list  
resultList = list(result)  
print(resultList)  
  
# Two iterables are passed  
result = zip(numList, strList)  
  
# Converting itertor to set  
resultSet = set(result)  
print(resultSet)  


### COPY
import copy

list1 = [1, 2, [3, 4, 5], 6]

shallow_copy_list = copy.copy(list1)  # shallow copy
list2 = list1   # also a shallow copy
deep_copy_list = copy.deepcopy(list1)  # deep copy

print("Original list: ", list1)
print("Shallow copied list: ", list2)

# Making modifications to the deep copy
deep_copy_list[2][1] = 9
print("Modified deep copy list: ", deep_copy_list)
print("Original list after modification to deep copy: ", list1)

# Making modifications to shallow copy
shallow_copy_list[2][1] = 6
print("Modified shallow copy list: ", shallow_copy_list)
print("Original list after modification to shallow copy: ", list1)
