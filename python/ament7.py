import Calculator as c
import datetime
import time


# print(c.add(1,2,3,4))
# print(c.mul(5,6))
# print(c.div(5,0))
# print(c.sub(5,0))
import Shapes as s
# print(s.peri_circle(9))
# print(s.peri_square(9))
# print(s.peri_rectangle(4,9))
# print(s.area_circle(9))
# print(s.area_square(9))
# print(s.area_rectangle(4,9))
# di={}
# with open('Sales/Jan.csv','r') as Jan:
#     for line in Jan:

# stu_data={
#     'Name':'Saksham',
#     'E-mail':'saksham.dhillon.ug20@nsut.ac.in',
#     'Age':21,
#     'DOB':19-9-2002,
#     'Roll no:':'2020UCA1806',
#     'Address':'V.P.O Banipur,Bawal,Rewari',
#     'Department':'Computer Science',
#     'Current-Year':2,
#     'Specilisation':'A.I',

# }


# import json
# #from jsonschema import validate, ValidationError

# def validate_and_clean(json_data):
#     cleaned_data=[]
#     for d in json_data:
#         c={}
#         for k in d:
            
#             if(k=="age"):
#                 c[k]=int(d[k])
#             if(k=="is_student"):
#                 c[k]=bool(d[k])
#             if(k=="grades"):
#                 c[k]=[int(i) for i in d[k]]
#         cleaned_data.append(c)
#     return cleaned_data
# # json_data = {
# #     "name": "Saksham",
# #     "age": "21",
# #     "city": "Rewari",
# #     "is_student": "true",
# #     "grades": ["95", "87", "91"]
# # }

# # Validate and clean the JSON data
# with open('stu_data.json','r') as file:
#     json_data=json.load(file)
# cleaned_data = validate_and_clean(json_data)

# if cleaned_data:
#     print("Cleaned Data:")
#     print(cleaned_data)
# else:
#     print("Invalid Data.")
##################################################################
# import csv

# def calculatetotalsales(csv_files):
#     final={}
#     for month in csv_files:
#         with open(month,'r') as m_file:
#             m_dict=csv.DictReader(m_file)
#             for row in m_dict:
#              product=row['Product']
#              sales=int(row['sales'])
#              if(final.get(product,0)==0):
#                 final[product]=sales
#              else:
#                 final[product]+=sales
            
#     return final
# li=['Sales/Jan.csv','Sales/Feb.csv']
# final_ans=calculatetotalsales(li)
# for key,value in final_ans.items():
#     print(f"{key}:{value}")
##############################################
#Q3 OS MODULE
import os

current_dir=os.getcwd()
print("Current Directory:",current_dir)

file_list=os.listdir(current_dir)
print("Files and Directory in current Directory:",file_list)

file_path=os.path.join(current_dir,'sample.txt')
if os.path.exists(file_path):
    print("File Exists:",file_path)

file_size=os.path.getsize(file_path)
print("File Size:",file_size,"bytes")

os.remove(file_path)
print("File is Removed")
#Q3 SYS module
import sys

print("Python Version:",sys.version)

print("Platform Information",sys.platform)

print("Maximum Integer size:",sys.maxsize)


data=sys.stdin.readline()
print("Input:",data)

sys.stdout.write("Hello My Name is Saksham\n")

sys.stderr.write("Error Please Try Again")

print("Memory Size:",sys.getsizeof([1,2,3]))
#Q3 DateTime
import datetime

curr=datetime.datetime.now()
print("Current Time",curr)

d=datetime.date(2022,2,16)
print("Specific Date",d)

t=datetime.time(12,30,0)
print("Specific Time",t)

duration=datetime.timedelta(days=5,seconds=3600)
print("Duration:",duration)

date_str = "2024-02-20 12:00:00"
p_d = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", p_d)

t=datetime.time(12,0,0)
print("Specific Time",t)
duration=datetime.timedelta(days=5,seconds=3601)
print("Duration:",duration)
date_str = "2024-02-20 12:00:00"
parsed_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_datetime)
from collections import namedtuple,deque,Counter,OrderedDict,defaultdict
#named Tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print("Named tuple:", p)
print("Accessing named tuple fields:", p.x, p.y)
# deque
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print("Deque:", d)
print("Deque length:", len(d))
print("Deque pop:", d.pop())
print("Deque pop left:", d.popleft())
# Counter
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)
print("Word counts:", word_counts)
print("Most common word:", word_counts.most_common(1))
# OrderedDict
d = OrderedDict([('a', 1), ('c', 2), ('d', 3)])
print("OrderedDict:", d)
print("Keys in OrderedDict:", list(d.keys()))
# defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print("Defaultdict:", d)
print("Accessing key not present in defaultdict:", d['c'])
print("Defaultdict after accessing key not present:", d)
#Q3 re Module
import re
#re Modules in Python provide Support for working with Regular Expression which is PowerFul tool for Pattern Matching and Text Processing
pattern=r'hello'
string='hello world'
match=re.match(pattern,string)
if match:
    print("Matches Found")
else:
    print("Match Not Found")
#for Search
pattern=r'world'
string='helloworld'
match=re.search(pattern,string)
if match:
    print("Yes Pattern is found in String")
else:
    print("No Pattern is Not found")
#non overlapping string
pattern = r'hello'
string = 'hello hello world'
matches = re.findall(pattern, string)
print("All matches:", matches)

pattern = r'\d+'
string = 'Today is 2024-02-20'
replacement = 'YYYY-MM-DD'
new_string = re.sub(pattern, replacement, string)
print("New string:", new_string)

pattern = re.compile(r'hello')
string = 'hello world'
match = pattern.match(string)
if match:
    print("Match found:", match.group())
else:
    print("No match")
import sqlite3
# Connect to the database
conn = sqlite3.connect('crud_operations.db')
cursor = conn.cursor()
# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
conn.commit()
def create_user(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
def read_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def update_user(user_id, new_name, new_email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (new_name, new_email, user_id))
    conn.commit()
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
# Example usage
create_user('ram', 'ram@gmail.com')
create_user('rahul', 'rahul@gmail.com')
read_users()
update_user(1, 'Yash', 'yash@gmail.com')
read_users()
delete_user(2)
read_users()
# Close connection
conn.close()



