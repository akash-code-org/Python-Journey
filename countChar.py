n = input('enter the string: ')
term = input('which letter would you like to find: ')
count = 0
for i in n:
    if i == term:
        count += 1

print('Frequency is: ',count)

# This code counts the particular character in the string