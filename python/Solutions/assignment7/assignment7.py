#Modules and Packages

#1 CALCULATOR
import calculator as c

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

print("Enter the operation:")
print("1: Add\n2: Subtract\n3: Multiply\n4: Divide")

try:
    operation = int(input("Choose operation (1/2/3/4): "))
except ValueError:
    print("Invalid input. Please enter a valid operation.")
    exit()

try:
    result = {1: c.add(a, b), 2: c.sub(a, b), 3: c.mul(a, b), 4: c.div(a, b)}
    print("Result:", result[operation])
except ZeroDivisionError as e:
    print(f"Error: {e}")




#2 SHAPES
from Shapes import circle, rectangle, square, triangle

# Circle
radius = 5
circle_area = circle.area(radius)
circle_perimeter = circle.perimeter(radius)
print(f"Circle - Area: {circle_area:.2f}, Perimeter: {circle_perimeter:.2f}")

# Square
side = 4
square_area = square.area(side)
square_perimeter = square.perimeter(side)
print(f"Square - Area: {square_area:.2f}, Perimeter: {square_perimeter:.2f}")

# Triangle
base = 8
height = 6
triangle_area = triangle.area(base, height)
triangle_perimeter = triangle.perimeter(3, 4, 5)
print(f"Triangle - Area: {triangle_area:.2f}, Perimeter: {triangle_perimeter:.2f}")

# Rectangle
length = 7
width = 5
rectangle_area = rectangle.area(length, width)
rectangle_perimeter = rectangle.perimeter(length, width)
print(f"Rectangle - Area: {rectangle_area:.2f}, Perimeter: {rectangle_perimeter:.2f}")




#3 os, sys, datetime, collections and re

# --- os Module ---
import os

dir_path = "/Users/ananyapaliwal/Downloads"
files = os.listdir(dir_path)
print("Files in directory:", files)

current_dir = os.getcwd()
print("Current working directory:", current_dir)

new_dir_path = "/Users/ananyapaliwal/Downloads/new"
os.mkdir(new_dir_path)
print("Directory created:", new_dir_path)

path_to_check = "/Users/ananyapaliwal/Downloads/assignment7"
is_directory = os.path.isdir(path_to_check)
print(f"{path_to_check} is a directory: {is_directory}")

old = "/Users/ananyapaliwal/Downloads/test.py"
new = "/Users/ananyapaliwal/Downloads/test1.py"
os.rename(old, new)
print("File renamed:", new)


# --- sys Module ---
import sys

add = 0
n = len(sys.argv) 
for i in range(1, n): 
    add += int(sys.argv[i]) 
print("the sum is :", add) 

print("Exiting program.")
#sys.exit()

python_version = sys.version
print("Python version:", python_version)

max_int_size = sys.maxsize
print("Maximum integer size:", max_int_size)

platform = sys.platform
print("Platform:", platform)

# --- datetime Module ---
from datetime import date, time, datetime, timedelta
# Date module
my_date = date(2020, 12, 11) 
print("Date passed as argument is ", my_date)

# Time module
my_time = time(12, 14, 36)
print("Entered time", my_time)
my_time = time(minute = 12)
print("\nTime with one argument", my_time)
my_time = time()
print("\nTime without argument", my_time)

# DATETIME
print("Min DateTime supported", datetime.min)
print("Max DateTime supported", datetime.max)
print('The current date and time', datetime.now())

#Timedelta
obj = timedelta(hours=1)
print(obj.total_seconds())

current_datetime = datetime.now()
print('Cuurent date and time: ', datetime.strftime(current_datetime, "%Y-%m-%d %H:%M:%S"))
future_datetime = current_datetime + timedelta(weeks=3)
print("Future Date and Time:", future_datetime)
print('Difference: ', future_datetime - current_datetime)

weekday = current_datetime.strftime("%A")
print("Weekday:", weekday)

# Parse String to Datetime

date_str = "2022-01-01"
time_str = "09:30:45"
combined_str = f"{date_str} {time_str}"
parsed_date = datetime.strptime(combined_str, "%Y-%m-%d %H:%M:%S")
print("Parsed date:", parsed_date)


# --- collections Module ---
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque
# Counter
data = [1, 2, 3, 1, 2, 4, 5, 1, 2, 3, 5, 4]
counter = Counter(data)
print("Counter:", counter)

# DefaultDict
default_dict = defaultdict(int)
default_dict['a'] = 1
print(default_dict['b'], default_dict)

# NamedTuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person(name='John', age=25, city='New York')
print("NamedTuple:", person)

# OrderedDict
ordered_dict = OrderedDict({'a': 1, 'b': 2, 'c': 3})
print("OrderedDict:", ordered_dict)

# Deque
deque_example = deque([1, 2, 3])
deque_example.append(4)
deque_example.appendleft(0)
print("Deque:", deque_example)


# --- re Module ---
import re
# Match
pattern_match = re.compile(r'\d+')
match_result = pattern_match.match('123abc')
print("Match:", match_result.group() if match_result else "No match")

# Search
pattern_search = re.compile(r'\d+')
search_result = pattern_search.search('abc123def')
print("Search:", search_result.group() if search_result else "No match")

# Find All
pattern_find_all = re.compile(r'\d+')
find_all_result = pattern_find_all.findall('abc123def456')
print("Find All:", find_all_result)

# Substitution
pattern_substitution = re.compile(r'\d+')
substitution_result = pattern_substitution.sub('X', 'abc123def456')
print("Substitution:", substitution_result)

# Split
pattern_split = re.compile(r'\d+')
split_result = pattern_split.split('abc123def456')
print("Split:", split_result)




#FILES

#4 CSV FILES
import os
import csv

def extract_and_aggregate(folder_path):
    agg_data = {}

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    prod = row['Product']
                    sales = float(row['Sales'])

                    if prod in agg_data:
                        agg_data[prod] += sales
                    else:
                        agg_data[prod] = sales

    summary_path = os.path.join(folder_path, 'summary_report.csv')
    with open(summary_path, 'w', newline='') as summary_file:
        csv_writer = csv.writer(summary_file)
        csv_writer.writerow(['Product', 'Total Sales'])
        for prod, total_sales in agg_data.items():
            csv_writer.writerow([prod, total_sales])

    print(f'Summary report generated and saved at: {summary_path}')

    with open(summary_path, 'r') as summary_file:
        print("Generated Summary Report:")
        print(summary_file.read())

# Example usage:
folder_path = '/Users/ananyapaliwal/Downloads/assignment7/csv'
extract_and_aggregate(folder_path)




#5 JSON DATA
import json

def validate_clean_data(json_data):
    required_keys = ['username', 'email', 'age', 'city', 'active']

    cleaned_data = []

    for entry in json_data:
        if all(key in entry for key in required_keys):
            try:
                cleaned_entry = {
                    'username': str(entry['username']),
                    'email': str(entry['email']),
                    'age': int(entry['age']),
                    'city': str(entry['city']),
                    'active': bool(entry['active'])
                }
                cleaned_data.append(cleaned_entry)
            except (ValueError, TypeError) as e:
                print(f"Invalid entry: {entry}. Error: {e}. Skipping...")
        else:
            print(f"Entry missing required keys: {entry}. Skipping...")

    return cleaned_data

json_file_path = '/Users/ananyapaliwal/Downloads/assignment7/example.json'

try:
    with open(json_file_path, 'r') as json_file:
        user_data = json.load(json_file)

    cleaned_user_data = validate_clean_data(user_data)

    print("Cleaned User Data:")
    for entry in cleaned_user_data:
        print(entry)

except FileNotFoundError:
    print(f"File not found: {json_file_path}")
except json.JSONDecodeError:
    print(f"Invalid JSON format in file: {json_file_path}")




#6 CRUD - SQL AND NOSQL
import sqlite3
from pymongo import MongoClient

# SQLite Database Configuration
sqlite_conn = sqlite3.connect('example.db')
sqlite_cursor = sqlite_conn.cursor()

# MongoDB Atlas Configuration
mongo_conn_str = "mongodb+srv://ananyapaliwal123:ananyapaliwal123@example.p84nwhe.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(mongo_conn_str)
mongo_db = mongo_client['example_db']
mongo_collection = mongo_db['Example']

# Create Table or Collection
def create():
    # SQLite
    sqlite_cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    ''')
    sqlite_conn.commit()

# Insert Data
def insert():
    # SQLite
    sqlite_cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John', 25))
    sqlite_conn.commit()

    # MongoDB
    mongo_collection.insert_one({'name': 'John', 'age': 25})

# Read Data
def read():
    # SQLite
    sqlite_cursor.execute("SELECT * FROM users")
    sqlite_data = sqlite_cursor.fetchall()
    print("SQLite Data:", sqlite_data)

    # MongoDB
    mongo_data = list(mongo_collection.find())
    print("MongoDB Data:", mongo_data)

# Update Data
def update():
    # SQLite
    sqlite_cursor.execute("UPDATE users SET age = ? WHERE name = ?", (30, 'John'))
    sqlite_conn.commit()

    # MongoDB
    mongo_collection.update_one({'name': 'John'}, {'$set': {'age': 30}})

# Delete Data
def delete():
    # SQLite
    sqlite_cursor.execute("DELETE FROM users WHERE name = 'John' ")
    sqlite_conn.commit()

    # MongoDB
    mongo_collection.delete_one({'name': 'John'})

create()
insert()
read()
update()
read()
delete()
read()

# Close Database Connections
sqlite_conn.close()
mongo_client.close()
