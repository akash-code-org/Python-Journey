def func_1(x):
    def func_2(x):
        x = x+1
        print(x)
    x = x+1
    print(x)
    func_2(x)
    return x

x = 3
z = func_1(x)