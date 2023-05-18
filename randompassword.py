import string
import random

def generate_random_password(length, input_letters, input_number, input_special_character):
    generated_password = ""
    final_password = ""
    if input_letters == "y" or input_letters == "Y":
        generated_password += string.ascii_letters
        final_password = random.choice(string.ascii_letters)
     
    if input_number == "y" or input_number == "Y":
        generated_password += string.digits
        final_password += random.choice(string.digits)
     
    if input_special_character == "y" or input_special_character == "Y":
        generated_password += string.punctuation
        final_password += random.choice(string.punctuation)

    password = "".join(random.choice(generated_password) for _ in range(length))
    final_password += password
    return final_password[:length]

def main():
    length = 0
    while length <= 3:
        length = int(input("Input Length for Password (greater than 2): "))
        if length <= 3:
            print("Length should be greater than 2.")
    input_letters = input("Would Like to add letters (y/n) ")
    input_number = input("Would Like to add number (y/n) ")
    input_special_character = input("Would Like to add special character (y/n) ")
    password = generate_random_password(length, input_letters, input_number, input_special_character)
    if password:
        print("Your New Password is = "+ password)
main()
