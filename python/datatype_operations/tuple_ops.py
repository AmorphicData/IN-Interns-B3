myTuple = 1, 2, 3, 4
print (myTuple)

# 1. Packing a tuple
tuple_1 = 1, 2, 3  # No need for parentheses
print(tuple_1)# (1, 2, 3)
tuple_2 = ('a', 'b', 'c')
print(tuple_2)# ('a', 'b', 'c')

# 2. Unpacking a tuple
a, b, c = tuple_1
print(a, b, c)# 1 2 3
x, y, z = tuple_2
print(x, y, z)# a b c

#1. Accessing tuple using index
example = "apple", "orange", "banana", "berry", "mango"
print (example[0])

#2. Adding elements to a tuple
t = (1, 2, 3, 4, 5)
t = t + (7,)
print(t)

#3. Deleting a tuple
del (myTuple)

#4. Slicing a tuple
t = (1, 2, 3, 4)
print(t[2:4])

#5. Multiplication
t = (2, 5)
print (t*3)

#6. len, min and max function
t = (1, 4, 2, 7, 3, 9)
print (len(t))
print (max(t))
print (min(t))

#7. Trying to modify tuple using index swhich will raise error
my_tuple1 = (1,2,3)
tuple[1]=10 #This will raise an error

#8. Converting list to tuples
my_tuple1 = (1,2,3)
list1 = list(my_tuple1) # converting tuple to list
list1[1] = 10 # modifying the list
my_tuple1 = tuple(list1) #convert to tuple
print(my_tuple1)