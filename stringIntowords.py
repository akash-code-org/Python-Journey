s = input('Enter the string: ') # Dividing string into words:
L = []
temp = ''
for i in s:
    if i != ' ':
        temp+=i
    else:
        L.append(temp)
        temp = ''
L.append(temp)
print(L)