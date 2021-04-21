def decorator_func(any_func):
    def wrapper_func(*args, **kwargs):
        print("this is awesome function")
        return any_func(*args, **kwargs)
    return wrapper_func
@decorator_func
def add(a, b):
    return a + b
print(add(2, 3))