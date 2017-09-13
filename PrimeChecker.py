num = int(input("\nEnter a number to be checked : "))
flag = 0
divisible_by = [1]
for i in range(2, int(num/2) + 1):
    if (num % i) == 0:
        divisible_by.append(i)
        flag = 1

divisible_by.append(num)

if flag == 1:
    print("\n" + str(num) + " is not a prime number. \nDivisible by : " + str(divisible_by))
else:
    print("\n" + str(num) + " is prime number.")