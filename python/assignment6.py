#Question 1 Logging
'''
def log_call(func):
    def modify(*args):
        print(f"Calling this function: {func.__name__} with args: {args}")
        result= func(*args)
        print(f"Function {func.__name__} completed with result: {result}")
        return result
    return modify

@log_call
def adding(*args):
    sum=0
    for i in args:
        sum += i
    return sum

res = adding(3,4,5,6)
print(res)
'''


#Question 2 Retry Mechanism
'''
def retry(func):
    def modify(*args,**kwargs):
        max_attemp=2
        for i in range(max_attemp):
            try:
                ans=func(*args,**kwargs)
                return ans
            except Exception as e:
                print(f"Retry failed due to {e} . Retrying ")
    return modify

@retry
def divide(a,b):
    return a/b
ans2=divide(6,3)
print(ans2)
ans3=divide(6,0)
print(ans3)

'''
#Question 3 Authorization

'''
allowed_user=['ceo', 'admin','manager']
def authorize(function):
    def modify(*args):
        for i in args:
            if i in allowed_user:
                return function(*args)
            else:
                print("Unauthorized user")
    return modify
@authorize
def check(user):
    print(f"Information about the user: {user}")

def main():
        check('admin')
        check('abc')
main()

'''

#Question 4 Rate Limiting
'''
curr=0
def rate_limiting(func):
    def modify(*args,**kwargs):
       max_limit_allowed=5
       global curr #it will refer to global curr and take that value
       if  curr<max_limit_allowed:
           ans=func(*args,**kwargs)
           
           return ans
       else:
           raise Exception("Rate Limit Exceed")
    return modify
@rate_limiting
def fun():
    print("Heavy Tasking Ongoing")

def main():
    try:
        fun()
        fun()
        fun()
        fun()
        fun()
        fun()
    except Exception as e:
        print(e)

main()
'''

#Question 5 Input Validation

'''
def validate_input(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                print(f"Error: {arg} is not a valid input. It must be an integer or a float.")
                return None
        return func(*args)
    return wrapper

@validate_input
def calculate_sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

result1 = calculate_sum(5, 3,'asf')
print("Result 1:", result1)

result2 = calculate_sum(5, 3, 2)
print("Result 2:", result2)  
'''


#Question 6
'''
def cache(func):
    cached_results = {}

    def wrapper(*args):
        if args in cached_results:
            print(f"Result already found for {args} in cache!")
            return cached_results[args]
        else:
            result = func(*args)
            cached_results[args] = result
            return result

    return wrapper



@cache
def added(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum

print(added(3))
print(added(6))
print(added(10))
print(added(6))
print(added(5))
print(added(5))
'''


