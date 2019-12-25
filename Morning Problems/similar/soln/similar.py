# Read in the input
a,b,c = map(int, input().split())

# Solve the problem and output the result
if a == b and a == c and b == c:
	print("same")
elif a == b or a == c or b == c:
	print("similar")
else:
	print("distinct")
	