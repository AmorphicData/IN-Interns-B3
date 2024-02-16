#q1 - Write a program that reads a string (paragraph) and performs various text analysis tasks such as counting the number of words, counting the frequency of each word, finding the longest word, etc.

def text_analysis(paragraph):
    # Counting the number of words
    words = paragraph.split()
    num_words = len(words)
    print(f"Number of words: {num_words}")

    # Counting the frequency of each word
    word_frequency = {}
    for word in words:
        word = word.lower() 
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    print("\nWord frequency:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

    # Finding the longest word
    longest_word = max(words, key=len)
    print(f"\nLongest word: {longest_word}")


text_analysis("Welcome to Cloudwick Welcome to Banglore ")


#q2 - Write a simple calculator program that takes user input for arithmetic operations (+, -, *, /) and performs the calculations. Use loop to continuously prompt the user for input until they choose to exit the program, and include error handling to handle invalid inputs

def calculator():
    while True:
        
        print("\nSimple Calculator:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        
        if choice == '5':
            print("Exit the calculator.")
            break

        
        try:
            num1 = float(input("Enter the first num: "))
            num2 = float(input("Enter the second num: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue


        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
calculator()

#q3 - Write a program that generates a calendar for a specified month and year.
import calendar
def generate_calendar():
    
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

   
    if not (1 <= month <= 12):
        print("Invalid month. Please enter a month between 1 and 12.")
        return

    
    cal = calendar.monthcalendar(year, month)

    
    print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
    print(" Mo Tu We Th Fr Sa Su")
    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end=" ")
            else:
                print(f"{day:2d}", end=" ")
        print()  

generate_calendar()


#q4 - Write a program that generates random passwords of a given length using uppercase letters, lowercase letters, numbers, and special characters

import random

def generate_password(length):
    
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_characters = '!@#$%^&*()_-+=|;:,.<>?'

    
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    
    if length < 8:
        print("Password length should be at least 8 characters.")
        return

    
    password = ''.join(random.choice(all_characters) for _ in range(length))


    print(f"Generated Password: {password}")

length = int(input("Enter the desired password length: "))
generate_password(length)


#q5 - Create a program that manages inventory for a store. Use loop to continuously prompt the user for actions such as adding, updating, or removing items from the inventory.

def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def add_item(inventory):
    item_name = input("Enter the name of the item to add: ")
    quantity = int(input("Enter the quantity to add: "))

    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

    print(f"{quantity} {item_name}(s) added to the inventory.")

def update_item(inventory):
    item_name = input("Enter the name of the item to update: ")

    if item_name in inventory:
        new_quantity = int(input("Enter the new quantity: "))
        inventory[item_name] = new_quantity
        print(f"{item_name} quantity updated to {new_quantity}.")
    else:
        print(f"{item_name} not found in the inventory.")

def remove_item(inventory):
    item_name = input("Enter the name of the item to remove: ")

    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print(f"{item_name} not found in the inventory.")

inventory = {}
while True:
        print("\nOptions:")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_item(inventory)
        elif choice == '3':
            update_item(inventory)
        elif choice == '4':
            remove_item(inventory)
        elif choice == '5':
            print("Exiting the inventory management system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


