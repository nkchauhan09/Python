def func(l, **kwargs):
    if kwargs.get("rev_string") == True:
        return [i[::-1].title() for i in l]
    else: return[i.title() for i in l] 
print(func(["neeraj", "kumar", "chauhan"], rev_string = True)) 