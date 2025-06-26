winning_num = 50
user_input = int(input("Guess the number between 1 to 100: "))

if user_input == winning_num:
    print("Congrats,You WIN !")
else:
    if user_input < winning_num:  #nested if-else
        print("too low")
    else:
        print("too high")