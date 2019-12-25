num_matches = int(input())

rA = 0
rB = 0
for i in range(num_matches):
    round_list = input().split()
    A = 0
    B = 0
    for j in round_list:
        if j == 'RS': 
            A = A + 1
        if j == 'PR':
            A = A + 1
        if j == 'SP':
            A = A + 1

        if j == 'SR':
            B = B + 1
        if j == 'RP':
            B = B + 1
        if j == 'PS':
            B = B + 1
    if A > B:
        rA += 1
    if B > A:
        rB += 1
    if B == A:
        rA += 0
        rB += 0

if rA > rB:
    print("Alice",rA)
elif rB > rA:
    print("Bob",rB)
elif rB == rA:
    print("Alice",rA)
        
# print here whoever is the overall winner of all the matches and
# how many matches the winner won
    


    

# print here whoever is the overall winner of all the matches and
# how many matches the winner won
