# WAP to add items os 2 list indexwise
L1 = [1,2,3]
L2 = [-1,-2,-3]
#result = []
#for i, j in zip(L1,L2):
#        result.append(i+j)

#print(result)

print([i+j for i,j in zip(L1,L2)])