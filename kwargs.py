def func(**kwargs):
    # print(name)
    print(kwargs)
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f"{k} : {v}")
func(first_name = "Neeraj", last_name = "Chauhan")
d = {"name" : "Neeraj", "age" : 23}
func(**d)