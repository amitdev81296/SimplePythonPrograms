def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

a, b = (int(x) for x in input("\nEnter the two integers : ").split())
print("\nGCD of " + str(a) + " and " + str(b) + " is " + str(gcd(a, b)))
