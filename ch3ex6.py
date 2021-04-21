import random
winning_num = random.randint(1, 100)
guess_num = int(input("Guess the number : "))
count = 1
# while True:  
for count in range(1, 101): 
    if guess_num < winning_num:
        print("Too Low")
    elif guess_num > winning_num:
        print("Too High")
    else:
        print(f"You Win ......... You guessed number in {count} attempts")
        break
    guess_num = int(input("Guess again : "))
    # count += 1