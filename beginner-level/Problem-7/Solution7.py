def find_missing(numbers):
    n = len(numbers) + 1  # Expected length including missing number
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

# Test the function
input_list = [1, 2, 4, 5]
print(find_missing(input_list))