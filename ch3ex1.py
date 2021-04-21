winning_number = 25
guess_number = int(input("Enter a number from 1 to 30 : "))
if winning_number == guess_number:
    print("YOU WIN !!!!")
else:
    if winning_number > guess_number:
        print("Too Low")
    else:
        print("Too High")