
# Python code to demonstrate the use of default arguments    
# defining a function    
def function( n1, n2 = 20 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
     
     
# Calling the function and passing only one argument    
print( "Passing only one argument" )    
function(30)    
    
# Now giving two arguments to the function    
print( "Passing two arguments" )    
function(50,30)    