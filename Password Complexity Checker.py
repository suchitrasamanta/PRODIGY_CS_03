import re

def check_password_strength(password):
    # Initialize feedback variables
    length_error = "Password must be at least 8 characters long."
    uppercase_error = "Password must contain at least one uppercase letter."
    lowercase_error = "Password must contain at least one lowercase letter."
    number_error = "Password must contain at least one number."
    special_error = "Password must contain at least one special character."
    
    # Validate password length
    if len(password) < 8:
        return "Weak", length_error
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Weak", uppercase_error
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Weak", lowercase_error
    
    # Check for at least one number
    if not re.search(r'\d', password):
        return "Weak", number_error
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak", special_error
    
    # If all checks pass
    return "Strong", "Password is strong and secure."

# Example usage
password = input("Enter a password to check its strength: ")
strength, message = check_password_strength(password)
print(f"Password strength: {strength}")
print(f"Feedback: {message}")
