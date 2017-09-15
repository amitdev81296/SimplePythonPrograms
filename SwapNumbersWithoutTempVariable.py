a,b = (int(x) for x in input("\nEnter the values of a and b : ").split())

print("\nBefore Swapping\na = " + str(a) + "\nb = " + str(b))

a = a + b
b = a - b
a = a - b

print("\nAfter Swapping\na = " + str(a) + "\nb = " + str(b))