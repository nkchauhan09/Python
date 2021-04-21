while True:
    try:
        age = int(input("enter your age : "))
        break
    except ValueError:
        print("please enter age in integer....")
    except:
        print("unexpected error....")
if age < 18:
    print("you can't play this game")
else:
    print("you can play this game")