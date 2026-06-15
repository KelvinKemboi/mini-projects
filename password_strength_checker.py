import re
def check_password_strength(password):
    if len(password) < 8:
        return "Password is too short"
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter"
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter"
    if not re.search(r"\d", password):
        return "Password must contain at least one digit"
    if not re.search(r"[!@#$%^&*()-+]", password):
        return "Password must contain at least one special character"
    return "Password is strong"

# Example usage
password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print(result)
