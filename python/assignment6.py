#1 - Logging
def logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@logging
def mul(x, y):
    return x * y

mul(10, 20)




#2 - Retry Mechanism
def retry(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Error occurred: {e}. Retrying...")
            raise Exception("Maximum retries exceeded. Function failed.")
        return wrapper
    return decorator

@retry(max_retries=3)
def example(a, b):
    if a + b < 0:
        raise ValueError("Sum is negative")
    return a + b

try:
    result = example(3, -4)
    print(f"Result: {result}")
except Exception as e:
    print(f"Exception caught: {e}")




#3 - Authorization
def authorize(user_roles):
    def decorator(func):
        def wrapper():
            if set(user_roles).issubset(set(roles())):
                return func()
            else:
                raise PermissionError("Unauthorized. Insufficient roles.")
        return wrapper
    return decorator

def roles():
    return ['admin', 'editor']

@authorize(user_roles=['admin', 'user'])
def f1():
    print("Executing f1.")

try:
    f1()
except PermissionError as e:
    print(f"PermissionError: {e}")




#4 - Rate Limiter
import time

def rate_limits(max_calls, period):
    def decorator(func):
        calls = 0
        last_reset = time.time()

        def wrapper():
            nonlocal calls, last_reset
            elapsed = time.time() - last_reset

            if elapsed > period:
                calls = 0
                last_reset = time.time()

            if calls >= max_calls:
                raise Exception('Maximum number of rate limits exceeded')
            calls += 1
            time.sleep(1)
            return func()

        return wrapper
    return decorator

@rate_limits(max_calls=6, period=10)
def api_call():
    print("API call executed successfully...")

for _ in range(8):
    try:
        api_call()
    except Exception as e:
        print(f"Error occurred: {e}")




#5 - Input validation
def validate(func):
    def wrapper(*args, **kwargs):
        if all(arg > 0 for arg in args):
            return func(*args, **kwargs)
        else:
            raise ValueError("Invalid arguments passed to the function. All arguments must be positive.")

    return wrapper

@validate
def multiply(a, b):
    return a * b

try:
    result1 = multiply(5, -3)
    print(f"Result 1: {result1}")
except ValueError as e:
    print(f"Error: {e}")




#6 - Caching Function Results
def cache(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())
        if key in cache:
            print("Retrieving result from cache...")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@cache
def multiply(x, y):
    print("Calculating the product of two numbers...")
    return x * y

print(multiply(4, 5))
print(multiply(4, 5))
