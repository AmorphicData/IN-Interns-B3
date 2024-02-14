ls =[True,False,True,False,False,True,True,True]
print(ls)
print("All:" , all(ls))                  #Use of all(1)
print("Any:" , any(ls))                  #Use of any

# using bin to get binary of a integer
print("Binary value of 8: ", bin(8))
# Using bytes to get bytes object for a int
print("Byte obejct of integer 8" , bytes(8))
#Using evaluate
print("Evaluating 7 times 4" , eval("7*4"))
#Using execute
exec('print("Sum of 764 and 42 is(via execute) ", (764+42))')
#Using divmod
print("Quotient and Remainder: " , divmod(245,23))
#Using hex to convert int to hex
print("Hexadecimal value of 343221: " , hex(343221))
#Using oct to convert int to octal
print("Octal value of 343221: ",oct(343221))
#Using ord to get ascii value of a char(10)
print("ASCII value of A: ",ord('A'))
#Using round to round off
print("Rounding off 89.3452",round(89.3452))

#Using in built module functions
#getting a random number between 1 and 100
import random
print("Printing random value between 1 and 100: ",random.randint(1,100))
#Getting a random choice
fruits = ["Apple", "Avocado", "PineApple", "Kiwi"]
print("Printing a random fruit from a list: " , random.choice(fruits))

#Importing math module
#Square root of a number
import math
print("Root of 221:", math.sqrt(221))
#Printing PI
print("PI:", math.pi)

#Importing date
#Using date.today to get today's date
import datetime
print("Date Today: ",datetime.date.today()) 
#Using datetime.now to get timestamp
print("Timestamp: " , datetime.datetime.now())

#Using reversed to get reverse iterator of a list
print("Reversed list of first 8 natural numbers: " , list(reversed([1,2,3,4,5,6,7,8])))

#Using inbuilt sum function
print("Sum of first 8 natural numbers: " , sum([1,2,3,4,5,6,7,8]))

#Using help to get info about a function(20)
# print(help(pow))

#Using map to use a function taking a single input on a list
def trip(i):
    return i*3
lt = [1,2,3,4]
res = map(trip, lt)
print("Tripling the value of each element of [1,2,3,4] via map: " , list(res))

#Using complex to print a complex number
print("Complex number: " , complex(5,8))

#Using chr to get character out of ASCII
print("Character at 97: " , chr(97))

#Using ascii command to find all type of escape or special characters
tstr = '''Check
for
newline'''
print("Check for special and newline characters: " , ascii(tstr))

#Using type to identify datatype of a input(25)
print(type((1,2,3,4)))
print("=====================================================")


def custom_len(lst : list) -> int:
    ans = 0
    for i in lst:
        ans+= 1
    return ans

def custom_range(st, end, step=1):
    res = []
    curr = st
    if step > 0:
        while curr < end:
            res.append(curr)
            curr += step
    elif step < 0:
        while curr > end:
            res.append(curr)
            curr += step
    else:
        raise ValueError("Step cannot be zero")
    return res

def custom_strip(s : str)-> list:
    ans = ""
    for i in range(custom_len(s)):
        ans += ("" if s[i] == " " else s[i])
    return ans

def custom_max(*args):
    maxi = args[0]
    for i in args:
        maxi = (i if maxi < i else maxi)
    return maxi

def custom_min(*args):
    mini = args[0]
    for i in args:
        mini = (i if mini > i else mini)
    return mini

def power(s,n):
    if s != 0:
        while n > 1:
            s *=s
            n-=1
        return s
    else:   return 0

def custom_sum(*arg):
    sum=0
    for i in arg:
        sum+=i
    return sum

def custom_sort(*args):
    if len(args) <= 1:
        return args
    else:
        pivot = args[0]
        less = tuple(x for x in args[1:] if x <= pivot)
        greater = tuple(x for x in args[1:] if x > pivot)
        return custom_sort(*less) + (pivot,) + custom_sort(*greater)
    
def custom_split(s,delim=None)-> list:
    if delim==None: delim = " "
    res = []
    curr = ""
    for i in s:
        if i == delim:
            res += [curr]
            curr = ""
        else:
            curr += i
    res += [curr]
    return res

def custom_sqrt(n):
    if n < 0:
        raise ValueError("Negative value")
    g = n/2
    small = 1e-10
    while g * g - n > small or n - g * g > small:
        g = 0.5 * (g + n/g)
    return g
    
print(custom_len([5,4,7,3,6,7,4,4,2]))
print(custom_range(0,20,3))
print(custom_strip("Hello   guys this    function that  strips"))
print(custom_sum(5,3,3,5,6,8,6,4))
print(custom_max(5,34,67,234,79,342,67,2))
print(custom_min(5,34,67,234,79,342,67,2))
print(custom_sort(54,78,23,7,12,78,34,89,56))
print(custom_split("Hello Guys This is for the custom split"))
print(custom_sqrt(30))
print(power(7,4))
