# Python code to demonstrate the use of keyword arguments    
  # Defining a function    
def function( n1, n2 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
    
# Calling function and passing arguments without using keyword    
print( "Without using keyword" )    
function( 50, 30)       
        
# Calling function and passing arguments using keyword    
print( "With using keyword" )    
function( n2 = 50, n1 = 30)   