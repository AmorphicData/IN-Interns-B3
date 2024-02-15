'''
#  An example Python Function  
def function_name( parameters ):  
    # code block  
'''

# Example Python Code for User-Defined function  
def square( num ):    
    """  
    This function computes the square of the number.  
    """    
    return num**2     
object_ = square(6)    
print( "The square of the given number is: ", object_ )


# Python code to demonstrate the use of return statements      
# Defining a function with return statement    
def square( num ):    
    return num**2    
     
# Calling function and passing arguments.    
print( "With return statement" )    
print( square( 52 ) )    
    
# Defining a function without return statement     
def square( num ):    
     num**2     
    
# Calling function and passing arguments.    
print( "Without return statement" )    
print( square( 52 ) )    