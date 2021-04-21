def decorator_func(func):
    def wrapper_func():
        print("this is awesome function")
        func()
    return wrapper_func
def func1():
    print("this is function 1")
@decorator_func
def func2():
    print("this is function 2")
func1 = decorator_func(func1)
func1()
func2()
