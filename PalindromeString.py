s = input("Enter the string: ") # String letters should be same from both side start to end
flag = True
for  i in range(0,len(s)//2):
    if s[i] != s[len(s)-i-1]:
        flag = False
        print('not palindrome: ')
        break
if flag:
    print('Palindrome: ')