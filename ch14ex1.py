from functools import wraps
import time
def calc_time(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        print(f"executing {func.__name__} function")
        t1 = time.time()
        ret = func(*args, **kwargs)
        t2 = time.time()
        print(f"time taken is {t2 - t1}")
        return ret
    return wrapper_func
@calc_time
def func(n):
    return [i**2 for i in range(1, n + 1)]
print(func(10))

