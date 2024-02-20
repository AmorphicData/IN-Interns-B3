#Logging decorator
def log_call(func):
    def wrapper(*args):
        print(f"Calling function {func.__name__} with args: {args}")
        result = func(*args)
        print(f"Function {func.__name__} completed with result: {result}")
        return result
    return wrapper

@log_call
def adder(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

res = adder(3, 4, 7, 3, 9)
print(f"Result: {res}")

print("============================================================")

#Retry mechanism
def re_try(func):
    def wrapper(max_retries):
        attempts = 0
        while attempts < max_retries:
            try:
                return func()
            except Exception as e:
                attempts += 1
                print(f"Retry {attempts}/{max_retries}. Retrying...")
        print(f"Max retries reached. Giving up.")
    return wrapper

@re_try
def check(max_retries=5):
    import random
    if random.randint(0,1) == 0:
        raise Exception("Error here!")
    else:
        print("Success!")

check(2)

print("============================================================")

#Authorization Decorator
def authorization(func):
    req_perm = "admin"
    def wrapper(user_perm):
        if req_perm in user_perm:
            return func(user_perm=user_perm)
        else:
            raise PermissionError(f"Permission denied as user lacks '{req_perm}' permission.")
    return wrapper

@authorization
def admin_funct(user_perm):
    print(f"{user_perm} access here")
    print("Admin-only function executed.")

user_permissions = ["user", "admin"]
try:
    admin_funct(user_perm=user_permissions)
except PermissionError as e:
    print(f"PermissionError: {e}")

print("============================================================")

#Rate Limiting decorator
def rate_lim(func):
    def wrapper(st,end,step):
        if st > end/2 :
            print("Limiting the rate by half:")
            return func(st,end,int(step/2))
        else:
            print("No rate limiting is required.")
            return func(st,end,step)
    return wrapper

@rate_lim
def iterate(st,end,step):
    for i in range(st,end,step):
        print(i)

iterate(11,20,4)

print("============================================================")

#Input Validation decorator
def validate(func):
    def wrapper(val):
        global res
        print("Validating the provided input for integer values......")
        if type(val) == int:
            print(f"Valid data {val} found.")
        else:
            try:
                print("Attempting conversion value to integer")
                res = func(val)
                return res
            except ValueError:
                print("Input is not of integer type.")
    return wrapper

@validate
def Input_val(x):
    print(f"Input: {x}")
    ans = int(x)
    return ans

Input_val("cgh")

print("============================================================")

#Caching function results
import time
def cache(func):
    def wrapper(a , b):
        cache_file = 'cache_file.txt'
        try:
            with open(cache_file, 'r') as file:
                cache_data = dict(line.strip().split(':') for line in file)
        except FileNotFoundError:
            cache_data = {}
        key = f"{func.__name__}_{a}_{b}"
        if key in cache_data:
            res, elapsed_time = map(float, cache_data[key].split(','))
            print(f"Found {func.__name__}({a}, {b}) - Result: {res}, Time: {elapsed_time:.6f} seconds")
        else:
            start_time = time.time()
            res = func(a, b)
            elapsed_time = time.time() - start_time
            cache_data[key] = f"{res},{elapsed_time}"
            with open(cache_file, 'w') as file:
                for k, v in cache_data.items():
                    file.write(f"{k}:{v}\n")
            print(f"Cache miss for {func.__name__}({a}, {b}) - Result: {res}, Time: {elapsed_time:.6f} seconds")
        return res
    return wrapper

@cache
def adder(a , b):
    return a+b

@cache
def diff(a , b):
    return a-b
@cache
def mul(a , b):
    return a*b

@cache
def div(a , b):
    return a/b

print(adder(6,7))
print(diff(45,7))
print(div(63,7))
print(mul(6,7))