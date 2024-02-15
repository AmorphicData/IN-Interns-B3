# Question 6 - Calculator

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"


previous_result = None  # Variable to store the result of the previous calculation

while True:
    if previous_result is not None:
        continue_previous = input("Do you want to continue with the previous result? (yes/no): ").lower()
        if continue_previous == 'yes':
            num1 = previous_result
        else:
            num1 = float(input("Enter the first number: "))
    else:
        num1 = float(input("Enter the first number: "))

    operator = input("Enter the operator (+, -, *, /): ")

    if operator in ['+', '-', '*', '/']:
        num2 = float(input("Enter the second number: "))

        result = calculate(num1, operator, num2)
        print("Result:", result)

        previous_result = result  # Update the previous result variable
    else:
        print("Invalid operator. Please enter a valid operator.")

    exit_choice = input("Do you want to exit? (yes/no): ")
    if exit_choice.lower() == 'yes':
        print("Exiting program.")
        break


# Question 8 - Manage inventory for a store

inventory ={}

def add_item():
    item_name = input("Enter the name of the item: ")
    item_quantity = int(input("Enter the quantity of the item: "))
    inventory[item_name] = item_quantity
    print("%s added to inventory with quantity %s." % (item_name, item_quantity))

def update_item():
    item_name = input("Enter the name of the item you want to update: ")
    if item_name in inventory:
        new_quantity = int(input("Enter the new quantity: "))
        inventory[item_name] = new_quantity
        print("%s quantity updated to %s." % (item_name, new_quantity))
    else:
        print("Item not found in inventory.")

def remove_item():
    item_name=input("Enter the name of the item you want to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print("%s removed from inventory." % item_name)
    else:
        print("Item doesn't exist")

def display_inventory():
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print("%s: %s" % (item, quantity))

def main():
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Update item quantity")
        print("3. Remove item")
        print("4. Display inventory")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            display_inventory()
        elif  choice == "5":
            print ("Exiting Program")
            break
        else:
            print("Invalid Choice")
main()

# Question 7 - Banking System

accounts = {}

def create_account(name):
    accounts[name] = 0
    print("Account '%s' created successfully." % name)

def deposit(name, amount):
    if name in accounts:
        accounts[name] += amount
        print("Deposited %.2f into account '%s'. New balance: %.2f" % (amount, name, accounts[name]))
    else:
        print("Account not found.")

def withdraw(name, amount):
    if name in accounts:
        if accounts[name] >= amount:
            accounts[name] -= amount
            print("Withdrew %.2f from account '%s'. New balance: %.2f" % (amount, name, accounts[name]))
        else:
            print("Insufficient funds")
    else:
        print("Account not found.")

def transfer(sender, receiver, amount):
    if sender in accounts and receiver in accounts:
        if accounts[sender] >= amount:
            accounts[sender] -= amount
            accounts[receiver] += amount
            print("Transferred %.2f from account '%s' to '%s'" % (amount, sender, receiver))
        else:
            print("Insufficient funds")
    else:
        print("One or both accounts not found.")

def display_balance(name):
    if name in accounts:
        print("Balance of account '%s': %.2f" % (name, accounts[name]))
    else:
        print("Account not found.")
        
while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Display Balance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter account name: ")
        create_account(name)
    elif choice == '2':
        name = input("Enter account name: ")
        amount = float(input("Enter deposit amount: "))
        deposit(name, amount)
    elif choice == '3':
        name = input("Enter account name: ")
        amount = float(input("Enter withdrawal amount: "))
        withdraw(name, amount)
    elif choice == '4':
        sender = input("Enter sender's account name: ")
        receiver = input("Enter receiver's account name: ")
        amount = float(input("Enter transfer amount: "))
        transfer(sender, receiver, amount)
    elif choice == '5':
        name = input("Enter account name: ")
        display_balance(name)
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")


# Question 5 - Guessing Number

import random

def guess_number():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Number Guessing Game!")

    while attempts < max_attempts:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1

            if guess == number:
                print("Congratulations! You guessed the correct number in", attempts, "attempts!")
                break
            elif guess < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("Sorry, you've exceeded the maximum number of attempts. The correct number was:", number)


guess_number()


#Question 2 - Random Password

import random
import string

def generate_password(length):

    # uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    # numbers = '0123456789'
    # special_characters = '!@#$%^&*()_+{}[]|\\;:\'",.<>?'
    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_characters = string.punctuation
    
    all_characters = uppercase_letters + lowercase_letters + numbers + special_characters
    
    
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

password_length = int(input("Enter the length of the password: "))
generated_password = generate_password(password_length)
print("Generated password:", generated_password)







    