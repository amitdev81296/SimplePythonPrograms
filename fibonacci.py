n = int(input("Enter the number of terms : "))
fibonacci_sequence = []
first = 0
second = 1
next_term = 0

for i in range(0, n):
    if i <= 1:
        next_term = i
    else:
        next_term = first + second
        first = second
        second = next_term
    fibonacci_sequence.append(next_term)

print(fibonacci_sequence)
