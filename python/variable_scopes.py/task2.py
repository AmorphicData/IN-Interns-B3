# Python program to show how the nonlocal keyword works  
  
print ("Using the nonlocal keyword before changing a:")  
  
# Assigning 'a' in the global scope  
a = 0  
  
# Defining a function  
def outer():  
  
    # Giving new value to 'a' in the local scope of the 'outer' function  
    # Didn't use global keyword here  
    a = 3  
    def inner():  
  
        # Defining the variable scope as the local scope of the 'outer' function  
        nonlocal a   
  
        # Changing the value of 'a' in the local scope of the 'inner' function  
        a = 14  
  
        # Printing the value of 'a' in the local scope of the 'inner' function  
        print("Inside 'inner' function:- ", a)  
      
    # Calling the inner function  
    inner()  
  
    # Priting the value of 'a' inside the function  
    print("Inside the 'outer' function:- ", a)  
  
# Calling the main function  
outer()  
  
# Printing the value of 'a' in the global scope  
print("In the global scope:- ", a)  
  
# Performing the same steps as above without using the nonlocal keyword  
print ("\nNot using the nonlocal keyword before changing a:")  
  
# Assigning 'a' in the global scope  
a = 0  
  
def outer():  
    a = 3  
  
    def inner():  
  
        # Not using the nonlocal keyword before assigning a new value to a  
        a = 14  
        print("Inside 'inner' function:- ", a)  
  
    inner()  
    print("Inside the 'outer' function:- ", a)  
     
# Calling the main function  
outer()  
  
print("In the global scope:- ", a) 