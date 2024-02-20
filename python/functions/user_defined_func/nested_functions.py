# Python code to show how to access variables of a nested functions    
# defining a nested function    
def word():    
    string = 'Python functions tutorial'    
    x = 5     
    def number():    
        print( string )   
        print( x )  
             
    number()    
word()    