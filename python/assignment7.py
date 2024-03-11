#Question 1.1
calculator.py

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

def mul(a,b):
    return a*b

def sub(a,b):
    return a-b

def div(a,b):
    if (b==0):
        print("Cannot Divide by 0")
    else:
        return a/b


'''
import calculator
print("Perform Operations: ")
a = calculator.add(1,3,2,4,4)
b = calculator.mul(3,4)
c = calculator.sub(2,3)
d = calculator.div(4,3)
e=calculator.div(4,0)
print(a)
print(b)
print(c)
print(d)

'''
#Question 1.2
package shape

area.py

import math
def rect(l,b):
    return l*b

def circle(r):
    return math.pi*r*r

perimeter.py

import math
def rect(l,b):
    return 2*(l+b)

def circle(r):
    return 2*math.pi*r
'''
import shape.area as ar, shape.perimeter as peri
print("Print values: ")
cir1 = ar.circle(3)
cir2=peri.circle(3)
rect1 = ar.rect(4,5)
rect2= peri.rect(4,5)
print(cir1)
print(cir2)
print(rect1)
print(rect2)
'''

#Question 1.3

import os
import sys
import datetime
import collections
from collections import Counter
import re
# def os_module_functions():
#     print("Current Working Directory:", os.getcwd())
#     # 2. List files and directories in a directory
#     print("Files and Directories in Current Directory:")
#     print(os.listdir())
#     #current Directory
#     current_dir=os.getcwd()
#     print(current_dir)
#     # 3. Create a new directory
#     new_dir_name = "abcd"
#     os.mkdir(new_dir_name)
#     print(f"Directory '{new_dir_name}' created successfully")
#    
#     file_path=os.path.join(current_dir,'abc.txt')
#     print(file_path)

#     os.remove(file_path)
    

# res = os_module_functions()
# print(res)


# def sys_module_functions():
    
#     print("Python Version:", sys.version)
  
#     print("Platform:", sys.platform)
    
#     print("Maximum integer value in Python:", sys.maxsize)

#     sys.stdout.write("Hello!\n")
    
#     sys.exit("Exiting the program...")

# res = sys_module_functions()
# print(res)


# def datetime_module_functions():
#     # 1. Get the current date and time
#     current_date = datetime.datetime.now()
#     print("Current Date and Time:", current_date)
#     # 2. Format a date
    
#     print("Formatted Date:", current_date.strftime("%d-%h-%y"))
    
#     print("IsoCalender:", current_date.isocalendar())
#     # 4. Get the current year
#     print("Current Year:", datetime.datetime.now().year)
    
#     print("Day of the Week (Monday=0):", datetime.datetime.now().weekday())

# res = datetime_module_functions()
# print(res)


# from collections import *  
    
# With sequence of items   
# It is used to count the occurrences of elements in an iterable 
# counter = Counter(['B','B','A','B','C','A','B', 'B','A','C'])
# print(counter) 

# d1 = {'a': 1, 'b': 2} 
# d2 = {'c': 3, 'd': 4} 
  
# # Defining the chainmap  
# c = ChainMap(d1, d2)
# #print single value
# #print (c['a']) 

# initializing deque  
# de = deque((1,2,3))  
# # using append() to insert element at right end   
# # inserts 4 at the end of deque  
# de.append(4)   
# # printing modified deque  
# print ("The deque after appending at right is : ")  
# print (de)  
# # using appendleft() to insert element at left end   
# de.appendleft(6)  
# print(de)
# de.popleft()
# print(de)
#  maintains the order of insertion of key-value pairs.
# order_d = OrderedDict({'a':1, 'b':2, 'c':3, 'd':4})  
# print(order_d)

# Point = namedtuple('Point', ['x', 'y'])

# # Create an instance of the named tuple:
# p = Point(10, 20)

# print(p.x)  
# print(p.y)  


# def re_module_functions():

#     pattern = 'Hello'
#     text = "Hello! How are you Hello"
#     match = re.search(pattern, text)
#     if match:
#         print("Pattern found:", pattern)
#     else:
#         print("Pattern not found")

#     word_to_find = input("Enter the word to find: ")
#     matches = re.findall(word_to_find, "hello is a  ab12 is text with some words.")
#     if word_to_find in matches:
#         print("Word is present")
#     else:
#         print("Word is not present")
   
#     new_text = re.sub('is', '11', "hello is a text with some words.")
#     print("Replaced text:", new_text)
#     parts = re.split('this', "Split this string by this words")
#     print("Split parts:", parts)
    
# res = re_module_functions()
# print(res)


#Question 2.1
'''
import os
import pandas as pd
def extract(csv_file):
    df = pd.read_csv(csv_file)
    return df
def aggregate_dat(dataframes):
    aggregated_data = pd.concat(dataframes, ignore_index=True)
    return aggregated_data.groupby('Product')['Sales'].sum().reset_index()
def gen_report(aggregated_data):
    summary_report = aggregated_data.sort_values(by='Sales', ascending=False)
    return summary_report
def all_files(csv_directory):
    csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]
    dataframes = []
    for csv_file in csv_files:
        file_path = os.path.join(csv_directory, csv_file)
        dataframes.append(extract(file_path))
    agg_data = aggregate_dat(dataframes)
    summary_report = gen_report(agg_data)
    return summary_report
def main():
    dir = 'sample_data'
    res = all_files(dir)
    print(res)

main()
'''

#Question 2.2
'''
import json
# Define predefined rules for validation
mandatory_keys = {'name', 'age', 'email', 'address', 'phone'}
# Function to validate and clean JSON data
def validate_and_clean_data(json_data):
    cleaned_data = []
    for entry in json_data:
        cleaned_entry = {}
        for key in mandatory_keys:
            if key in entry:
                # Convert data to appropriate data types
                if key == 'age':
                    try:
                        cleaned_entry[key] = int(entry[key])
                    except ValueError:
                        print(f"Invalid age value '{entry[key]}' for entry: {entry}")
                        break
                elif key == 'phone':
                    # Remove non-numeric characters from phone number
                    cleaned_entry[key] = ''.join(filter(str.isdigit, entry[key]))
                else:
                    cleaned_entry[key] = entry[key]
            else:
                print(f"Missing mandatory key '{key}' for entry: {entry}")
                break
        # If all mandatory keys are present, add the cleaned entry
        if len(cleaned_entry) == len(mandatory_keys):
            cleaned_data.append(cleaned_entry)
    return cleaned_data
# Sample JSON data (replace this with your actual JSON data)
json_data = [
    {"name": "Nayan", "age": "21", "email": "nayan@gmail.com", "address": "Surya Royal Homes Oliva", "phone": "9910678787"},
    {"name": "abc", "age": "21", "email": "abc@gmail.com", "address": "Gurgaon"},
    {"name": "Ayush", "email": "ayush@gmail.com", "address": "Manipal", "phone": "959907891", "gender":"male"},
    {"name": "Raghav", "age": "21", "email": "raghva@gmail.com", "address": "Surya Royal Homes Oliva", "phone": "93255411yyyy111"},
]
# Validate and clean the data
cleaned_data = validate_and_clean_data(json_data)
# Print cleaned data
print("\nCleaned Data: \n")
print(cleaned_data)

'''

#Question 3


import sqlite3


# Function to create a new table
def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email )''')
    conn.commit()
    conn.close()

# Function to insert a new record
def insert_user(id, name, age, email):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (id, name, age, email) VALUES (?, ?, ?, ?)", (id,name, age, email))
    conn.commit()
    conn.close()

# Function to fetch all records
def fetch_all_users():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return rows

# Function to update a record
def update_user(id, name, age, email):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("UPDATE users SET name=?, age=?, email=? WHERE id=?", (name, age, email, id))
    conn.commit()
    conn.close()

# Function to delete a record
def delete_user(id):
    print(f"Deleting User with id: {id}")
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    # os.remove('example.db')
    conn.close()

# Create table
create_table()

# Insert records
insert_user(3, "John Doe", 25, "john@example.com")
insert_user(4, "Jane Smith", 30, "jane@example.com")

# Fetch and print all records
print("All users:")
print(fetch_all_users())

# Update a record
update_user(1, "John Smith", 26, "john.smith@example.com")

# Fetch and print all records after update
print("All users after update:")
print(fetch_all_users())

# Delete a record
delete_user(2)

# Fetch and print all records after delete
print("All users after delete:")
print(fetch_all_users())








