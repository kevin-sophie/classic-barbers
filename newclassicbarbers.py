

def is_valid_name(name):
    if not name or len(name.strip()) < 2:
        return False
    for char in name:
        if not (char.isalpha() or char.isspace()):
            return False
    return True


def is_valid_email(email):
    if not email or '@' not in email or '.' not in email:
        return False

    parts = email.split('@')
    if len(parts) != 2:
        return False

    local, domain = parts
    if not local or not domain or '.' not in domain:
        return False

    domain_parts = domain.split('.')
    if any(not part.isalnum() for part in domain_parts):
        return False
    return True


def is_valid_phone(number):
    if not number or not number.startswith('+'):
        return False
    digits = number[1:]  # Remove '+'
    if not digits.isdigit():
        return False
    if len(digits) < 11 or len(digits) > 15:
        return False
    return True


# Example usage
name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number with country code (e.g., +12345678901): ")

if is_valid_name(name):
    print("✅ Name is valid.")
else:
    print("❌ Invalid name.")

if is_valid_email(email):
    print("✅ Email is valid.")
else:
    print("❌ Invalid email.")

if is_valid_phone(phone):
    print("✅ Phone number is valid.")
else:
    print("❌ Invalid phone number.")


