import random
import string

# Getting the password length from the user
def get_password_length() -> int:
    while True:
        try:
            passwordLength = int(input("Enter the length of the password: \n-> "))
            if passwordLength < 8:
                print("Password length must be at least 8 characters.")
            else:
                return passwordLength
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Getting the password strength from the user
def get_password_strength() -> str:
    strengthType = ['1', '2', '3', 'weak', 'medium', 'strong']
    while True:
        try:
            passwordStrength = input("\nEnter the strength of the password:\n1. Weak\n2. Medium\n3. Strong\n-> ")
            for strength in strengthType:
                if passwordStrength in strength:
                    return strength
            else:
                print("Invalid input. Please enter a valid option.")
        except Exception as e:
            print(f"An error occured. {e}")

# Generating a weak password
def get_weak_password(password_length) -> str:
    password = ''
    for i in range(password_length):
        password += random.choice(string.ascii_letters)
    return password

# Generating a medium password
def get_medium_password(password_length) -> str:
    password = ''
    for i in range(password_length):
        password += random.choice(string.ascii_letters + string.digits)
    return password

# Generating a strong password
def get_strong_password(password_length) -> str:
    password = ''
    for i in range(password_length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

# Calling functions for generating a random password based on the user's input
def random_password() -> str:
    password = ''
    password_length = get_password_length()
    password_strength = get_password_strength()

    match password_strength:
        case '1' | 'weak':
            password = get_weak_password(password_length)
        case '2' | 'medium':
            password = get_medium_password(password_length)
        case '3' | 'strong':
            password = get_strong_password(password_length)
        case _:
            print("An Error Occured!")
    return password

# Main function to run the program
def main():
    password = random_password()
    print(f"\nGenerated Password:\n{password}\n")

if __name__ == "__main__":
    main()