#Question 1
'''
def analyze(paragraph):
    # Counting the number of words
    words = paragraph.split()
    num_words = len(words)
    print("Number of words:", num_words)

    words_freq = {}
    for word in words:
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word]= 1
    print("\nWord Freaquency: ")
    # for word, count in words_freq.items():
    #     print(f"{word}: {count}")
    print(words_freq)

    # Finding the longest word
    longest_word = max(words, key=len)
    print("\nLongest word:", longest_word)

    # Finding the average word length
    sum=0
    for word in words:
        sum += len(word)
    avg_length = sum/ num_words
    print("\nAverage word length:", avg_length)

paragraph="Hello how are you hello hello nbr bye bye bye hello hello guey bye bye"
analyze(paragraph)
'''
'''
#Question 2
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        random_character = random.choice(characters)
        password += random_character
    return password
    

def main():
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Error: Length must be a positive integer.")
            return
        password = generate_password(length)
        print("Generated Password:", password)

main()

'''

#Question 4
'''
import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 8
    print("Guess the number")

    while attempts<max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break

    if attempts >= max_attempts:
        print(f"Limit is exceeded. The correct number was {secret_number}.")
        

guess_the_number()

'''

#Question 5

def calculator(num1, num2, operator):
    if operator == '+' :
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"
      
def main():
    while True:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /) or 'exit' to quit: ")
            if operator == 'exit':
                print("Exit Pressed")
                break
            else:
                result = calculator(num1, num2, operator)
                print("Result:", result)

main()
    



#Question 7
'''
def display_inventor(inventory):
    print("Current Inventory")
    for item, qty in inventory.items():
        print(f"{item}: {qty}")

def add_item(inventory):
    print("What you want to add: ")
    item = input()
    qty = int(input("Enter the quantity: "))
    inventory[item] = inventory.get(item, 0) + qty
    print(f"{qty} {item}(s) added to inventory.")

def update_item(inventory):
    item = input("Enter the item to update: ")
    if item in inventory:
        qty = int(input("Enter the new quantity: "))
        inventory[item] = qty
        print(f"Inventory updated: {item} quantity set to {qty}.")
    else:
        print("Item not found in inventory.")

def remove_item(inventory):
    item = input(("Enter item ypu want to delete: "))
    if item in inventory:
        del inventory[item]
        print(f"{item} removed")
    else:
        print("Item not found")
    


def main():
    inventory={}
    while True:
        print("Choose Operation")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Exit")
        print("Enter your choice: ")
        opr = int(input())
        if opr==1:
            print("Printing Inventory: ")
            display_inventor(inventory)
        elif opr == 2:
            add_item(inventory)
        elif opr == 3:
            update_item(inventory)
        elif opr == 4:
            remove_item(inventory)
        elif opr == 5:
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice")


main()
'''
