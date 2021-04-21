while True:
    try:
        num = int(input("enter integer : "))
    except ValueError:
        print("please enter integer")
    except:
        print("unexpected error")
    else:
        print(f"entered number : {num}")
        break
    finally:
        print('finally block')