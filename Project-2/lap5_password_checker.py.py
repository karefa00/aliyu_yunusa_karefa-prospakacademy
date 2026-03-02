#  Password Checker with Logic and List Validation

# Get Password
password = input("Enter your password: ")

# Initialize Flags
has_min_length = False
has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

# Special characters for optional challenge
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Check Minimum Length
if len(password) >= 8:
    has_min_length = True

# Check for Character Types
for char in password:
    if char.isupper():
        has_uppercase = True
    if char.islower():
        has_lowercase = True
    if char.isdigit():
        has_digit = True
    if char in special_chars:
        has_special = True

    # Optimization: stop early if all conditions met
    if has_uppercase and has_lowercase and has_digit and has_special:
        break

# Provide Feedback
feedback_messages = []

if not has_min_length:
    feedback_messages.append("Password must be at least 8 characters long.")

if not has_uppercase:
    feedback_messages.append("Password must contain at least one uppercase letter.")

if not has_lowercase:
    feedback_messages.append("Password must contain at least one lowercase letter.")

if not has_digit:
    feedback_messages.append("Password must contain at least one digit.")

if not has_special:
    feedback_messages.append("Password must contain at least one special character.")

# Overall Status
if not feedback_messages:
    print("Password is strong!")
else:
    print("Password needs improvement:")
    for message in feedback_messages:
        print(message)