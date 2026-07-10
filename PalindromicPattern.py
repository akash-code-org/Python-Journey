n = int(input("Enter the numbre: "))
for i in range(1,n+1):
    a = i-1
    for j in range(1,i+1):
        print(j,end="")
    for k in range(1,i+1-1):
        print(a,end='')
        a-=1
    print()