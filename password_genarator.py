import random
import string

length=input("Enter your password length: ")
all=int(length)

lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
punctuation=string.punctuation

character=lower+upper+digit+punctuation

password=""

for i in range(all):
    a=random.choice(character)
    password+=a

print(password)
