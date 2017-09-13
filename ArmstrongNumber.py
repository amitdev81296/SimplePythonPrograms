print("***** Armstrong Number *****")
n = int(input("\nEnter the range : "))
armstrong_sequence = []
for i in range(0, n+1):
    sum = 0
    num_string = str(i)
    num_length = len(num_string)

    for j in range(0, num_length):
        sum = sum + int(num_string[j]) ** 3

    if sum == i:
        armstrong_sequence.append(i)

print(armstrong_sequence)