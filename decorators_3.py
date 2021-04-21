from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        """ this is wrapper function """
        print("this is awesome function")
        return any_func(*args, **kwargs)
    return wrapper_func
@decorator_func
def add(a, b):
    """ this is add function """
    return a + b
print(add(2, 3))
print(add.__name__)
print(add.__doc__)