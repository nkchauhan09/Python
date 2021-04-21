def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError:
        print('please enter integer or float')
    except:
        print("unexpected error")
print(divide(4, "3"))