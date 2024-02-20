# Q1 Logging

import time
def logging_decorator(fx):
    def modifying_func(*args):
        start_time = time.time()
        print(f"Logging: {fx.__name__}() called with args: {args}")
        ans=fx(*args)
        end_time = time.time()
        print(f"Function {fx.__name__}() took {end_time - start_time:.6f} seconds to execute.")
        return ans
    return modifying_func
@logging_decorator
def multiply(x,y):
    return x*y
ans2=multiply(3,5)
print("Result: ",ans2)

# Q3 Authorization

allowed_user={
    "Yash": "yash@123",
    "Kaustubh": "kaustubh@123",
    "Raj": "raj@123"
}
def authorization_decorator(fx):
    def modifying_func(**kwargs):
        user=kwargs.get('user')
        passwords=kwargs.get('passwords')
        if user in allowed_user and allowed_user[user] == passwords:
            return fx(**kwargs)
        else:
            raise PermissionError("Unauthorized user")
    return modifying_func
@authorization_decorator
def info(user, passwords):
    print("Login Successful")

def main():
    try:
        info(user='Yash',passwords='yash@123')
        info(user='Kaustubh',passwords='kaustubh')
    except PermissionError as e:
        print(e)

main()

# Q2 Retry Mechanism

allowed_user={
    "Yash": "yash@123",
    "Kaustubh": "kaustubh@123",
    "Raj": "raj@123"
}

def authorization_decorator(fx):
    def modifying_func(**kwargs):
        user = kwargs.get('user')
        passwords = kwargs.get('passwords')
        attempts = kwargs.get('attempts', 3)  # Defaulting to 3 attempts
        
        for attempt in range(attempts):
            if user in allowed_user and allowed_user[user] == passwords:
                return fx(**kwargs)
            else:
                if attempt < attempts - 1:
                    print(f"Login attempt {attempt + 1} failed. Retrying...")
                    user = input("Username: ")
                    passwords = input("Password: ")
                else:
                    raise PermissionError("Unauthorized user")
    return modifying_func

@authorization_decorator
def info(user, passwords):
    print("Login Successful")

def main():
    try:
        user = input("Username: ")
        passwords = input("Password: ")
        info(user=user, passwords=passwords)
    except PermissionError as e:
        print(e)

main()


# Q4 Rate Limiting (Limit the number of times function being called)

import time

def rate_limiting_decorator(func):
        last_called = [0]  # Using a list to store mutable value (time of last call)

        def wrapper(*args):
            limit_per_minute=args[0]
            current_time = time.time()
            if current_time - last_called[0] >= 60 / limit_per_minute: #Calculates the time interval allowed between function calls 
                last_called[0] = current_time
                return func(*args)
            else:
                print("Rate limit exceeded. Please wait before calling again.")

        return wrapper

@rate_limiting_decorator
def rate_limited_function(limit_per_minute):
    print("Function called at:", time.strftime("%H:%M:%S"))

for _ in range(3):
    rate_limited_function(6)
    time.sleep(5)  # To simulate time passing between function calls


#Q5 Input Validation

def input_validation():
    while True:
        user_input = input("Please enter a number between 1 and 100: ")
        try:
            num = int(user_input)
            if 1 <= num <= 100:
                return num
            else:
                print("Number must be between 1 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def Input_Validation_decorator(fx):
    def modifying_func(*args):
        validated_input = input_validation()
        return fx(validated_input, *args)
    return modifying_func

@Input_Validation_decorator
def Input_Validator(user_input):
    print("Valid input:", user_input)

Input_Validator()


#Q6 Caching function results

def caching_decorator(fx):
    cache = {}

    def modifying_func(n):
        if n not in cache:
            cache[n] = fx(n)
        return cache[n]

    return modifying_func

@caching_decorator
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120 (5!)
print(factorial(3))  # Output: 6 (3!)
print(factorial(5))  # Output: 120 (value retrieved from cache)
# If the value of n is found in the cache, the modifying_func returned by the 
# caching_decorator simply returns the cached result without recomputing it.