# Read the input
a, b, c = map(int, input().split())


# Solve the problem
average = (a + b + c) / 3

a = int(abs(a - average))
b = int(abs(b - average))
c = int(abs(c - average))
# Output the result
print(a, b, c)