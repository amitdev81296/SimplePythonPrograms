import random

num = int(input("Enter your number (between 0 and 10) : "))
while num not in range(0, 11):
    num = int(input("Error! Number must be between 0 and 10 : "))

random_int = random.randint(0, 11)

if num == random_int:
    print("\nLucky Asshole!!\n")
else:
    print("\nOops! Better Luck Next Time.")
