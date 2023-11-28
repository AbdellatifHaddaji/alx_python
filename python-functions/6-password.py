def validate_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter, one lowercase letter, and one digit
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not (has_upper and has_lower and has_digit):
        return False
    
    # Check for spaces
    if ' ' in password:
        return False
    
    return True

if __name__ == "__main__":
    print(validate_password("Password123"))
    print(validate_password("abc123"))
    print(validate_password("Password 123"))
    print(validate_password("password123"))