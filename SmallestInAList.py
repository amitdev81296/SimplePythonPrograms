input_string = input("Enter the list of numbers : ")
l = [int(x) for x in input_string.split(" ")]

print("\nThe max in the list is : " + str(min(l)))
