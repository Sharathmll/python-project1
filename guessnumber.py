import random
computer=random.randint(1,100)
a=-1
guess=1
while(a!=computer):
    a=int(input("Enter a number:   "))
    if a>computer:
        print(" Lower number please")
        guess+=1
    elif a<computer:
        print("Higher number please")
        guess+=1


print(f"You have guess the number {computer} in {guess} attempt")
    