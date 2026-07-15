n = int(input('Enter the number: ')) # converting integer into string
digits = '0123456789'
result = ''
while n != 0:
    result = digits[n%10]+result
    n//=10

print(result)
print(type(result))