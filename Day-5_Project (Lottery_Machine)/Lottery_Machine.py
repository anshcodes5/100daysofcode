print("Lottery Machine")
user_name = input("Welcome! What's your name?\nEnter here - ")
print(f"\nHi {user_name}!")

def lottery():
    
    user_input = int(input("enter a number from 1 to 5 to see if you win the lottery!\n"))
    
    import random
    lottery_num = random.randint(1, 5)

    if user_input == lottery_num:
        print("Congratulations! You won the lottery.")
        Replay = input('Type "R" to Replay!\nOr\nType "Q" to quit\n').lower()
        if Replay == "r":
            lottery()
        else:
            input("Thank you for playing! :)\ntype anything to close the program.")
    else:
        print("Oh you didn't win this time, better luck next time :)")
        Replay = input('Type "R" to Replay!\nOr\nType "Q" to quit\n').lower()
        if Replay == "r":
            lottery()
        else:
            input("Thank you for playing! :)\ntype anything to close the program.")
lottery()