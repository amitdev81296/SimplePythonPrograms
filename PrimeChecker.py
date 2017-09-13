num = int(input("\nEnter a number to be checked : "))
flag = 0
for i in range(2, int(num/2) + 1):
    if (num % i) == 0:
        flag = 1

if flag == 1:
    print("\n" + str(num) + " is not a prime number.")
else:
    print("\n" + str(num) + " is prime number.")