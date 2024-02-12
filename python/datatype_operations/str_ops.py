str = "HELLO"

#String Indexing
print(str[0])  
print(str[1])  
print(str[2])  
print(str[3])  
print(str[4])  
# It returns the IndexError because 6th index doesn't exist  
print(str[6])  
# Starts 2nd index to 3rd index  
print(str[2:4]) 

#Reassigning string - throws error since str is immutable
str = "HELLO"    
str[0] = "h"    
print(str) 

#deleting string item - throws error since str is immutable
str = "HELLO"  
del str[1]  

#deleting string
str1 = "HELLO"  
del str1  
print(str1)  


### escape sequence
# using triple quotes  
print('''''They said, "What's there?"''')  

# escaping single quotes  
print('They said, "What\'s going on?"')  

# escaping double quotes  
print("They said, \"What's going on?\"")  

print("C:\\Users\\DEVANSH SHARMA\\Python32\\Lib")  
print("This is the \n multiline quotes")  
print("This is \x48\x45\x58 representation")

print(r'C://python37') # prints C://python37 as it is written
###

### The format() method
# Using Curly braces  
print("{} and {} both are the best friend".format("Devansh","Abhishek"))  

#Positional Argument  
print("{1} and {0} best players ".format("Virat","Rohit"))  

#Keyword Argument  
print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky"))  
###

# Using % Operator
Integer = 10;    
Float = 1.290    
String = "Devansh"    
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(Integer,Float,String))    

# Using fstring
name = 'hello'
print(f"Hey !! {name}, welcome to the party...")


#String Concatenation
string1 = "hello"
string2 = "world "
string_combined = string1+string2
print(string_combined)

#string Repetition operator
string1 = "helloworld "
print(string1*2)
print(string1*3)
print(string1*4)
print(string1*5)

#string slicing operator
string1 = "helloworld"
print(string1[1])
print(string1[-3])
print(string1[1:5])
print(string1[1:-3])
print(string1[2:])
print(string1[:5])
print(string1[:-2])
print(string1[-2:])
print(string1[::-1])

#string comparison operator
string1 = "hello"
string2 = "hello, world"
string3 = "hello, world"
string4 = "world"
print(string1==string4)
print(string2==string3)
print(string1!=string4)
print(string2!=string3)


#string change to lower, upper case
string = "Various string methods"
string2 = "Investment in learning "
print("lower()")
print(string.lower())
print("\nupper()")
print(string.upper())

#string verify is it lower, upper case
print("\nislower()")
print(string.islower())
print("\nisupper()")
print(string.isupper())

#string check for starts with and ends with
print("\nstartswith")
print(string.startswith("Var"))
print("\nendswith()")
print(string.endswith("el"))

#string join
print("join()")
print('-->'.join(['various', 'strings', 'methods']))

#string split
print("\nsplit()")
print(string.split())

#string justify
print("\nljust()")
print("hello".ljust(15, '*'))
print("\nrjust(*)")
print("hello".rjust(15, '*'))
print("\ncenter()")
print("welcome".center(20, '*'))

#string strip
print("\nstrip()>")
print(string2.strip())
print("\nlstrip()")
print(string2.lstrip())
print("\nrstrip()")
print(string2.rstrip())

#string count
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print("&&&&%s", x)

#string index,count,find,replace
string = "object oriented orogramming"
print("Given String :", string)
print('\nindex()')
print("index of 'r' in:'", string, "':", string.index('r'))
print('\ncount()')
print("number of 'o' in '", string, "':", string.count('o'))
print('\nfind()')
print("index of 'z'in '", string, "':", string.find('z'))
print('\nreplace()')
print("replacing 'e' with '3' :", string.replace('e', '3'))



#check w3school and add more string operations if needed