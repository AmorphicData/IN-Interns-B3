# # Python code to demonstrate the use of variable-length arguments       
# # Defining a function    
# def function( *args_list ):    
#     ans = []    
#     for l in args_list:    
#         ans.append( l.upper() )    
#     return ans    
# # Passing args arguments    
# object = function('Python', 'Functions', 'tutorial')    
# print( object )    
    
# # defining a function    
# def function( **kargs_list ):    
#     ans = []    
#     for key, value in kargs_list.items():    
#         ans.append([key, value])    
#     return ans    
# # Paasing kwargs arguments    
# object = function(First = "Python", Second = "Functions", Third = "Tutorial")    
# print(object)   


def function( *x, **g ):    
    return x, g
# Passing args arguments    
object = function('hello', 'python', a='Python', b='Functions', c='tutorial')    
print( object ) 