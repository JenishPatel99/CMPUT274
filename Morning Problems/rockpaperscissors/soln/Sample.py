],['RP','SS'],['PS', 'RR', 'RP', 'PP', 'SS', 'RP', 'RR', 'SS', 'RP', 'SR'],['SR'],['RS', 'RP', 'PR'],['RP', 'SP', 'RP', 'RP', 'PP', 'RP', 'RR', 'SP', 'PP', 'PP', 'SR'],['PR', 'SS', 'SR', 'PP']]
rA = 0
rB = 0
for i in range(0,8):
    round_list1 = round_list[i]
    print(round_list1)
    print('list in list:', i)
    A = 0
    B = 0
    for j in round_list1:
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
    print(A, B)
    if A > B:
        rA += 1
    if B > A:
        rB += 1
    if B == A:
        rA += 0
        rB += 0
    print("rA", rA)
    print("rB", rB)

if rA > rB:
    print("Alice",rA)
elif rB > rA:
    print("Bob",rB)
elif rB == rA
    print("Alice",rA)
        
# print here whoever is the overall winner of all the matches and
# how many matches the winner won
    


    

# print here whoever is the overall winner of all the matches and
# how many matches the winner won
