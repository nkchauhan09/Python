def outer_func(msg):
    def inner_func():
        print(f"{msg} This is inner function")
    return inner_func
var = outer_func("hello")
var()

