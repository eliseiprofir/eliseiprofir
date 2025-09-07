import re
import secrets
import string


def generate_password(length: int = 16, nums: int = 1, special_chars: int = 1, uppercase: int = 1, lowercase: int = 1) -> str:

    # Define the possible characters for the password
    letters: str = string.ascii_letters
    digits: str = string.digits
    symbols: str = string.punctuation

    # Combine all characters
    all_characters: str = letters + digits + symbols

    while True:
        password: str = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints: list[tuple[int, str]] = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(constraint <= len(re.findall(pattern, password))
               for constraint, pattern in constraints):
            break
    
    return password


if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
