#for i in range(1,4):
#   for j in range(1,4):
#        print(i*j,end="") # [1, 2, 3, 2, 4, 6, 3, 6, 9]

print([i*j for i in range(1,4) for j in range(1,4)])