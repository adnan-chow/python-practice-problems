def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test the function
input_num = 5
print(factorial(input_num))