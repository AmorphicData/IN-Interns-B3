# Decorators

#Logging 

def log_function(func):
    def wrapper(*args):
        print(f"Perform {func.__name__} with arguments {args}")
        result=func(*args)
        return result
    return wrapper
@log_function
def add(a,b):
    return a+b

@log_function
def mul(a,b):
    return a*b


if __name__=="__main__":
    print(f"Result of add : {add(3,5)}")
    print(f"Result of mul : {mul(4,5)}")


#Retry Mechanism
    
import time
def retry(max_retries=5, delay_seconds=2):
    def decorator(func):
        def wrapper(*args):
            attempts = 0
            while attempts < max_retries:
                try:
                    result = func(*args)
                    return result
                except Exception as e:
                    print(f"Attempt {attempts + 1}/{max_retries} failed: {e}")
                    attempts += 1
                    time.sleep(delay_seconds)
            raise RuntimeError(f"Maximum retries ({max_retries}) reached. Unable to complete operation.")
        return wrapper
    return decorator

@retry(max_retries=5, delay_seconds=2)
def example_function():
    import random
    if random.random() < 0.3:
        raise ValueError("Random error")
    return "Success"

if __name__ == "__main__":
    result = example_function()
    print(f"Result: {result}")
    



#Authorization
    
USER_PERMISSIONS = {
    'user1': ['read'],
    'user2': ['read', 'write'],
    'admin': ['read', 'write', 'delete']
}

def authorize(permission):
    def decorator(func):
        def wrapper(user, *args):
            if permission in USER_PERMISSIONS.get(user, []):
                return func(user, *args)
            else:
                raise PermissionError(f"User '{user}' does not have permission to access this resource.")
        return wrapper
    return decorator

@authorize(permission='read')
def read_data(user):
    return f"{user} is reading data."

@authorize(permission='write')
def write_data(user):
    return f"{user} is writing data."

@authorize(permission='delete')
def delete_data(user):
    return f"{user} is deleting data."

if __name__ == "__main__":
    user1 = 'user1'
    user2 = 'user2'
    admin = 'admin'

    print(read_data(user1))
    print(write_data(user2))
    print(delete_data(admin))

#Rate Limiting (Limit the number of times function being called)
    

import time
def rate_limit(limit, interval):
    def decorator(func):
        last_called = None
        calls = 0

        def wrapper(*args):
            nonlocal last_called, calls
            if last_called is None or time.time() - last_called > interval:
                last_called = time.time()
                calls = 1
            else:
           
                if calls < limit:
                    calls += 1
                else:
                    print(f"Rate limit exceeded. Please wait before calling {func.__name__} again.")
                    return None

         
            result = func(*args)
            return result

        return wrapper
    return decorator


@rate_limit(limit=3, interval=10)  
def limited_function():
    print("Function executed.")


if __name__ == "__main__":
    for _ in range(5):
        limited_function()
        time.sleep(2)


#Input Validation
        
def validate_input(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Invalid input type: {type(arg)}. Only int or float are allowed.")


        return func(*args)
    return wrapper

@validate_input
def calculate_sum(a, b, c):
    return a + b + c

if __name__ == "__main__":
    try:
        #result = calculate_sum(3, 'hani', 2)
        result= calculate_sum(3,10.2,5)
        print(f"Result: {result}")
   
    except TypeError as e:
        print(f"Error: {e}")

#Caching function results
        
def cache_result(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Retrieving result from cache")
            return cache[args]

        result = func(*args)
        cache[args] = result

        return result

    return wrapper

@cache_result
def calculate_multiply(x, y):
    print("Calculating the product of two numbers")
    return x * y

print(calculate_multiply(4, 5))
print(calculate_multiply(4, 5))
print(calculate_multiply(5, 7))
print(calculate_multiply(5, 7))
print(calculate_multiply(-3, 7))
print(calculate_multiply(4, 5))

