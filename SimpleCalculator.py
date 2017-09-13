def add():
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    print("\nThe addition returned : " + str(a + b))


def subtract():
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    print("\nThe subtraction returned : " + str(a - b))


def multiply():
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    print("\nThe multiplication returned : " + str(a * b))


def divide():
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    print("\nThe division returned the following : ")
    print("Quotient : " + str(int(a / b)))
    print("Remainder : " + str(a % b))

i = 0

while i != 1:
    print("\n***** Simple Calculator *****")
    print("1. Add two numbers.")
    print("2. Subtract two numbers.")
    print("3. Multiply two numbers.")
    print("4. Divide two numbers.")
    choice = int(input("Select your choice : "))
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        divide()
    option = input("\nDo You Want To Continue? (Y/N)")
    if option == 'N' or option == 'n':
        i = 1
