from functools import wraps
def is_int(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if all([type(i) == int for i in args]):
            return func(*args, **kwargs)
        return("invalid argument")
    return wrapper
@is_int
def add(*args):
    total = 0
    for i in args:
        total += i
    return(total)
print(add(1, 2, 3, 4, "neeraj"))