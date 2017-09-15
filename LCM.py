def lcm(x, y):
    if x > y:
        minimum = a
    else:
        minimum = b
    while(1):
        if minimum % a == 0 and minimum % b == 0:
            return minimum
        minimum = minimum + 1

a, b = (int(x) for x in input("\nEnter the two integers : ").split())
print("\nLCM of " + str(a) + " and " + str(b) + " is " + str(lcm(a, b)))