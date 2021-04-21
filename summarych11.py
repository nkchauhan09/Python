def func(name, *args, last_name = "unknown", **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func("neeraj", 1, 2, 3, 4, last_name = "chauhan", a = 1, b = 2)