# Declaring dict
my_dictionary = {
    "name": "Alice",
    "age": 25,
    "occupation": "Software Engineer"
}
my_dictionary = dict([("name", "Alice"), ("age", 25), ("occupation", "Software Engineer")])

# Accessing items
age = my_dictionary["age"]
name = my_dictionary.get("name", "Unknown")
name = my_dictionary.get("name")


# Adding items
my_dictionary["favorite_color"] = "blue"
 

# Modifying items
my_dictionary["age"] = 26
 

# Removing items
del my_dictionary["favorite_color"]
 

# Dictionary Length
print(len(my_dictionary))
 

# Iterating over the keys in a dictionary
for key in my_dictionary:
    print(key)

for key in my_dictionary.keys():
    print(key)

# Iterate over the values in a dictionary
for value in my_dictionary.values():
    print(value)


# Iterating over both keys and values in a dictionary
for key, value in my_dictionary.items():
    print(f"{key}: {value}")


# Updating items
new_dictionary = {"favorite_color": "blue"}
my_dictionary.update(new_dictionary)


# Popping items
name = my_dictionary.pop("name")

# Pop item - withdraws a random item from the dictionary and delivers it as a tuple
key, value = my_dictionary.popitem()

# Clear Dict
my_dictionary.clear()

#Nested Dict
my_contacts = {
    "Alice": {
        "phone_number": "123-456-7890",
        "email_address": "alice@example.com"
    },
    "Bob": {
        "phone_number": "987-654-3210",
        "email_address": "bob@example.com"
    }
}

alice_phone_number = my_contacts["Alice"]["phone_number"]

#Sorting based on dict keys
for key in sorted(my_contacts.keys()):
    print(key)

#Sorting based on dict values
for value in sorted(my_contacts.values()):
    print(value)
