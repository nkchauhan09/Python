class NameTooShortError(ValueError):
    pass
def validate(name):
    if len(name) < 8:
        raise NameTooShortError("please enter big username")
username = input("enter username : ")
validate(username)
print(f"hello {username}")