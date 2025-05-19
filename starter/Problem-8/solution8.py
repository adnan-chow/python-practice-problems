def guessing_game():
    stored_number = 6
    user_guess = int(input("Enter a number (1-9): "))
    if user_guess == stored_number:
        print("Your Guess Is Correct!")
    elif user_guess < stored_number:
        print("your guess is almost there")
    else:
        print("your guess is higher")

# Example (run in an interactive environment)
guessing_game()