import random
import string

def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

length = int(input("Enter the length of the password: "))
print("Generated Password : ", password_generator(length))
