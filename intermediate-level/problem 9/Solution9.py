def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()" for c in password)
    return has_upper and has_lower and has_digit and has_special

# Test the function
input_password = "Passw0rd!"
print(is_valid_password(input_password))