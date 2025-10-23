import random 
import string 

length = input("Enter the desired password length: ")

while not length.isdigit() or int(length) <= 0:
    length = input("Please enter a valid positive number for password length: ")

length = int(length)

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase 
digits = string.digits
symbols = string.punctuation 

all_chars = lowercase + uppercase + digits +symbols

password = ""
for _ in range(length):
    password += random.choice(all_chars)


print("\nGenerated Password:", password)