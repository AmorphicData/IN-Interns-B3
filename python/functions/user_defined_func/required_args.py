# Python code to demonstrate the use of default arguments      
# Defining a function    
def function( n1, n2 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
    
# Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30    
print( "Passing out of order arguments" )    
function( 30, 20 )       
    
# Calling function and passing only one argument    
print( "Passing only one argument" )    
function( 30 )   