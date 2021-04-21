from functools import wraps
def function_details(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        print(f"you are calling {func.__name__} function")
        print(f"{func.__doc__}")
        return func(*args, **kwargs)
    return wrapper_func
@function_details
def add(a, b):
    """ this function adds two numbers """
    return a + b
print(add(4, 5))