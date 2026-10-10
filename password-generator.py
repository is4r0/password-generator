import random

def generate_password():
    """
    A strong password must be 12 characters containing at least:
    - 1 lowercase letter [a-z]
    - 1 uppercase letter [A-Z]
    - 1 digit [0-9]
    - 1 special character [!@#$%^&*()-+]
    """
    digits = list("0123456789")
    lowercase = list("abcdefghijklmnopqrstuvwxyz")
    uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    symbols = list("~`!@#$%^&*()_+-={}|[]\\;':\",./<>?")

    password_chars = [
        random.choice(digits),
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(symbols)
    ]

    all_chars = digits + lowercase + uppercase + symbols
    password_chars += random.choices(all_chars, k=8)

    random.shuffle(password_chars)
    return ''.join(password_chars)

if __name__ == "__main__":
    print("Generated Password:", generate_password())