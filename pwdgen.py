import string
import random
def generate_password(length, use_letters, use_capletters, use_numbers, use_symbols):
    characters = ""

    if use_capletters:
        characters += string.ascii_uppercase
    if use_letters:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("Password Generator")
print("------------------")
length = int(input("Enter the password length: "))
use_letters = input("Include letters (y/n)? ").strip().lower() == 'y'
use_capletters = input("Include capital letters (y/n)? ").strip().lower() == 'y'
use_numbers = input("Include numbers (y/n)? ").strip().lower() == 'y'
use_symbols = input("Include symbols (y/n)? ").strip().lower() == 'y'
password = generate_password(length, use_letters, use_capletters, use_numbers, use_symbols)
if password:
    print("Your generated password is: ", password)
