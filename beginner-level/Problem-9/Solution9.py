def sum_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Test the function
input_num = 9875
print(sum_digits(input_num))