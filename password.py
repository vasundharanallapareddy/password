import random

def generate_passwords(pwlengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for length in pwlengths:
        password = "".join(random.choice(alphabet) for _ in range(length))
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)

    return passwords

def replace_with_number(pword):
    num_replacements = random.randint(1, 2)
    for _ in range(num_replacements):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[:replace_index] + str(random.randint(0, 9)) + pword[replace_index + 1:]
    return pword

def replace_with_uppercase_letter(pword):
    num_replacements = random.randint(1, 2)
    for _ in range(num_replacements):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(num_passwords) + " passwords")

    password_lengths = []
    print("Minimum length of password should be 3")

    for i in range(num_passwords):
        length = int(input(f"Enter the length of Password #{i + 1}: "))
        if length < 3:
            length = 3
        password_lengths.append(length)

    passwords = generate_passwords(password_lengths)

    for i in range(num_passwords):
        print(f"Password #{i + 1} = {passwords[i]}")

if __name__ == "__main__":
    main()
