# Get the input
leftlane = list(input().split())
rightlane = list(input().split())
# now do something similar to get the list of vehicles in the right lane
# Solve the problem
new_list = [''] * (len(leftlane) + len(rightlane))
length = len(new_list)

counter = 0
if len(leftlane) < len(rightlane):
    for i in range(0,len(rightlane)):
        if i < len(leftlane):
            new_list[2*i] = leftlane[i]
            new_list[2*i + 1] = rightlane[i]
            counter = counter + 2
        else:
            new_list.append(rightlane[i])
if len(rightlane) < len(leftlane):
    for i in range(0,len(leftlane)):
        if i < len(rightlane):
            new_list[2*i] = leftlane[i]
            new_list[2*i + 1] = rightlane[i]
        else:
            new_list.append(leftlane[i])
elif len(rightlane) == len(leftlane):
    for i in range(0,len(rightlane)):
        new_list[2*i] = leftlane[i]
        new_list[2*i + 1] = rightlane[i]

while '' in new_list:
    new_list.remove('')
# Print the result
print(' '.join(new_list))