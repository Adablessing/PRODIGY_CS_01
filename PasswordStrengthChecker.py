import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Lowercase letter check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Number check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>).")
    
    # Strength assessment
    if strength == 5:
        return "Strong password!", feedback
    elif strength >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password!", feedback

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result, feedback = check_password_strength(password)
    print(result)
    for f in feedback:
        print("-", f)
