def calculator(command):
    parts = command.split()
    if len(parts) != 3:
        return "Invalid input"
    op, num1, num2 = parts
    num1, num2 = int(num1), int(num2)
    
    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    return "Unknown operation"

# Test the function
input_command = "add 5 7"
print(calculator(input_command))