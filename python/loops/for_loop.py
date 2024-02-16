'''
for iterator_var in sequence:
    statements(s)
	
Talk about for loop internal working:  iter() and next()
'''
n = 4
for i in range(0, n):
	print(i)

# Example with List, Tuple, String, and Dictionary Iteration Using for Loops in Python
print("List Iteration")
l = ["hello", "world", "!"]
for i in l:
	print(i)
print("\nTuple Iteration")
t = ("hello", "world", "!")
for i in t:
	print(i)
print("\nString Iteration")
s = "Hello"
for i in s:
	print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("%s %d" % (i, d[i]))
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
	print(i),


# Iterating by the Index of Sequences
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
	print(list[index])

# Using else Statement with for Loop in Python - NOT SENSE MUCH
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
	print(list[index])
else:
	print("Inside Else Block")

# NESTED LOOPS
'''
for iterator_var in sequence:
   for iterator_var in sequence:
       statements(s)
   statements(s)
'''

