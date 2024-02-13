### SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
amount = 10000
if(amount > 2999)
    print("Testing")
#Err Reason: Colon missing

### IndentationError
if(a<3): 
print("gfg")

### TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
x = 5
y = "hello"
z = x + y

### NameError: This exception is raised when a variable or function name is not found in the current scope.
a = 5
c = a + b

### Assertion Error
x = 1
y = 1
assert y == 0

### IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
l = ['a', 'b', 'c']
i = l[4]

### KeyError: This exception is raised when a key is not found in a dictionary.
d = {'Andrew': [1,5,9], 'Smith': [3,6,9]}
print(d['Alex'])

### ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
x = 'abc'
int(x)

### AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
x = 2
y = x.upper()

# IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
f = open("foo.txt")

# ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
b = 10000
a = b / 0
print(a)

# ImportError: This exception is raised when an import statement fails to find or load a module.
import example

