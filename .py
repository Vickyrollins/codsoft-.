import random
import string
def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if not characters:
        raise ValueError("No characters available to generate the password.")
    return ''.join(random.choice(characters) for _ in range(length))
if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    print("Generated password:", password)
