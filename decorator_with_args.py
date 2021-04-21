from functools import wraps
def is_datatype(data_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if all([type(i) == data_type for i in args]):
                return func(*args, **kwargs)
            return "invalid argument"
        return wrapper
    return decorator
@is_datatype(str)
def addstring(*args):
    s = ""
    for i in args:
        s += i
    return s
print(addstring("neeraj", "kumar", "chauhan"))