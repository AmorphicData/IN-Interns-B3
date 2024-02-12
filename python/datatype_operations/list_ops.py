# 1. append
my_list=[1,2,3]
my_list.append(9)
my_list.append(8)
print("The list after append() operation is: ",my_list)

# 2. Extend
my_list.extend([20,21])
print("The list after axtend() operator is: ",my_list)

# 3. insert
my_list.insert(5,30)
print("The list after insert() operator is: \n",my_list)

# 4. remove
my_list.remove(10)
print("The list after remove() operator is: \n",my_list)

# 5. pop
my_list.pop
print("The list after pop() operator is:\n",my_list)

# 6. slice
print("The elements of list in the range of 3 to 12 are:\n",my_list[3:12])

# 7. reverse
coding_list = ["code", "python", "data", "science"]  
coding_list.reverse()   #Reverse Function implemented
print(coding_list)

# 8. len, min & max
print("Length of the list is: ",len(my_list))
print("Maximum element in the list is: ",max(my_list))
print("Minimum element in the list is: ",min(my_list))

# 9. count
my_list.extend([10,20,22])
print("The list is: \n",my_list)
print("Number of times 21 is in the list are: ",my_list.count(20))

# 10. Concatenate
list_one = [100, 150, 200]
list_two = [900, 950, 800]
new_list = list_one + list_two   #new_list variable holds the concatenated list
print(new_list)

# 11. Multiply
list_one = [100, 150, 200]
list_two = list_one * 3   #Multiplied the list with 3
print(list_two)

# 12. index
list_one = [100, 150, 200]
print(list_one.index(100))   #Using index function for a list

# 13. sort
my_list=[8,10,4,1,3,19,11,9,20]
my_list.sort()
print("The list after sort() operator is: \n",my_list)

# 14. clear
list_one = [100, 150, 200]
list_one.clear()  #This clears all the elements present in the list
print(list_one)

# 15. copy
even_numbers = [2, 4, 6, 8]
value = even_numbers.copy()
print('Copied List:', value)