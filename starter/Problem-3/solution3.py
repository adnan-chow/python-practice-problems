def who_is_elder(age1, age2):
    if age1 > age2:
        print("First brother is elder.")
    elif age2 > age1:
        print("Second brother is elder.")
    else:
        print("Both are of the same age.")

# Example usage
who_is_elder(25, 30)
who_is_elder(40, 40)
who_is_elder(35, 28)