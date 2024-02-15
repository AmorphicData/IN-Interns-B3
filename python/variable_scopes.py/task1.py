# Python program to summarise the global and local variable scope.  
  
# Defining a variable in the global scope  
a = 'in the global scope'  
     
# This function will print the global variable because there does not exist any local variable 'a'  
def func():  
    print('Inside func(): ', a)  
     
# This function will print the value assigned to the local variable 'a'  
# Because we are not using the global keyword  
def local():      
    a = 'inside function local()'  
    print('Inside local(): ', a)  
     
# This function will modify the global variable because we are using the global keyword  
def global_():      
    global a  
    a = 'changed inside function global_()'  
    print('Inside global_() : ', a)  
     
# Calling the functions  
# Value of 'a' in global scope after each function call  
print('global: ', a)  
func()  
print('global: ', a)  
local()  
print('global: ', a)  
global_()  
print('global: ', a)  