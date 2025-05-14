import random
import string

def generate_passwords():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if length < 4:
        print("Password length must be at least 4 character.") 
        return
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    remainig_length = length - len(required_characters)
    passwords = required_characters

    for _ in range(remainig_length):
        character = random.choice(all_characters)
        passwords.append(character)

    random.shuffle(passwords)

    str_passwords = "".join(passwords)
    return str_passwords

passwords = generate_passwords()
print(passwords)
