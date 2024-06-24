import random
import string

def generate_password(length):
    lower= string.ascii_lowercase
    upper= string.ascii_uppercase
    digits= string.digits
    special_char= string.punctuation

    all_characters = lower + upper + digits + special_char

    password= ''. join(random.choice(all_characters) for i in range(length))
    return password

def main():
    length= int(input("Enter the desired length of the password:"))
    lower= input("Include lowercase letters? (yes/no): ")
    upper= input("Include uppercase letters? (yes/no): ")
    digits= input("Include numbers? (yes/no): ")
    special_char= input("Include symbols? (yes/no): ")

    password = generate_password(length)
    print("Generated Password:", password)

main()