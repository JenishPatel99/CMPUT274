# read the input
string_input = input()

# solve the problem
vowel_list = ['a','e','i','o','u']
string_mod = string_input.lower()
counter = 0
for i in string_mod:
	for j in vowel_list:
		if i == j:
			counter = counter + 1
# output the result
print(counter)