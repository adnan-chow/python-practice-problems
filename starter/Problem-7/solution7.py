def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"

# Example
print(fizz_buzz(15))  # Output: FizzBuzz
print(fizz_buzz(9))   # Output: Fizz
print(fizz_buzz(10))  # Output: Buzz
print(fizz_buzz(7))   # Output: Not a Fizz-buzz number