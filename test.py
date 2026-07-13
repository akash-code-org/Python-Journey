lower = int(input("Enter lower  number: "))
uper = int(input("Enter uper number: "))
for i in range(lower,uper+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            print(i)