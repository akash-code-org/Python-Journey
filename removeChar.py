#s = input("Enter the string: ") # aproach 1
#term = input('what would you like remove char: ')
#result = ''
#for i in s:
#   if i == term:
#        pass
#    else:
#        result+=i

#print('Removed ',result)

s = input("Enter the string: ") # aproach 1
term = input('what would you like remove char: ')
result = ''
for i in s:
    if i != term:
        result+=i

print('Removed ',result)