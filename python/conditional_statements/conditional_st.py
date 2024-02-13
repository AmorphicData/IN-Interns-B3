'''
if expression:  
    statement
'''
# Simple Python program to understand the if statement  
num = int(input("enter the number:"))         
# Here, we are taking an integer num and taking input dynamically  
if num%2 == 0:      
# Here, we are checking the condition. If the condition is true, we will enter the block  
    print("The Given number is an even number")

#Alternative Execution
'''
if expression:  
    statement
else:
    statement
'''

if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

#Chained Execution
'''
if expression 1:   
    # block of statements   
  
elif expression 2:   
    # block of statements   
  
elif expression 3:   
    # block of statements   
  
else:   
    # block of statements
'''

# Simple Python program to understand elif statement  
number = int(input("Enter the number?"))    
# Here, we are taking an integer number and taking input dynamically  
if number==10:    
# Here, we are checking the condition. If the condition is true, we will enter the block  
    print("The given number is equals to 10")    
elif number==50:  
# Here, we are checking the condition. If the condition is true, we will enter the block    
    print("The given number is equal to 50");    
elif number==100:    
# Here, we are checking the condition. If the condition is true, we will enter the block  
    print("The given number is equal to 100");    
else:    
    print("The given number is not equal to 10, 50 or 100");  

#Nested Conditionals
'''
if expression:   
    # block of statements   
else:
    if expression 2:   
        # block of statements   
  
    else:   
        # block of statements
'''
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


# tasks:
# Complex if else conditional program

#explain short circuit condition in if-else - Guardian Pattern


#add - single line if else
age = 20

# One-liner if-else statement
age_group = "Minor" if age < 18 else "Adult"

print(age_group)

a = 5
b = 6
c = 7

# m = a if a > b else (c if a > c else b)
# m = a if a > b else c if a > c else b