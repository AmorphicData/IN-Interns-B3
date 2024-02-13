# Declaring a set
Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)
Days2 = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
print(Days2)  

#Adding elements to a set
Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nAdding other months to the set...");    
Months.add("July");    
Months.add ("August");    
print("\nPrinting the modified set...");    
print(Months)   

#Updating elements to a set
Months.update(["July","August","September","October"])
print(Months)

# Using discard() method - will not throw error if item doesnt exist
months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.discard("January");    
months.discard("May");    
print("\nPrinting the modified set...");    
print(months)    

# Using remove() function - will throw error if item doesnt exist
months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.remove("January");    
months.remove("May");    
print("\nPrinting the modified set...");    
print(months)   

# Using pop() function
Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nRemoving some months from the set...");    
Months.pop();    
Months.pop();    
print("\nPrinting the modified set...");    
print(Months)

# Using clear() function
Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nRemoving all the items from the set...");    
Months.clear()    
print("\nPrinting the modified set...")    
print(Months)    

# Union Operator (|)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 | s2
print ("Union of s1 and s2: ", s3)
s3 = s1.union(s2)
print ("Union of s1 and s2: ", s3)

# Create three sets  
s4 = {14,15,6,7,8}  

# Find the common elements between the three sets  
common_elements = s1.union(s2, s4)  

# Print the common elements  
print(common_elements)  


# Intersection Operator (&)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 & s2
print ("Intersection of s1 and s2: ", s3)
s3 = s1.intersection(s2)
print ("Intersection of s1 and s2: ", s3)

# Create three sets  
s4 = {4, 2, 3} 

# Find the common elements between the three sets  
common_elements = s1.intersection(s2, s4)  
  
# Print the common elements  
print(common_elements)  

# The intersection_update() method - updates the original set with the intersection values
a = {"Devansh", "bob", "castle"}    
b = {"castle", "dude", "emyway"}
c = {"fuson", "gaurav", "castle"}    
    
a.intersection_update(b, c)    
    
print(a) 

# Difference Operator (-)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 - s2
print ("Difference of s1 - s2: ", s3)
s3 = s1.difference(s2)
print ("Difference of s1 - s2: ", s3)
s3 = s2 - s1
print ("Difference of s2 - s1: ", s3)

# Symmetric Difference Operator
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 - s2
print ("Difference of s1 - s2: ", s3)
s3 = s2 - s1
print ("Difference of s2 - s1: ", s3)
s3 = s1 ^ s2
print ("Symmetric Difference in s1 and s2: ", s3)
s3 = s1.symmetric_difference(s2)
print ("Symmetric Difference in s1 and s2: ", s3)

#check w3school and add more set operations if needed