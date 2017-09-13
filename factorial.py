number = int(input("\nEnter a number : "))
factorial = 1
for i in range(1, number+1):
    factorial = factorial * i
print("\nThe factorial of the " + str(number) + " is " + str(factorial))
