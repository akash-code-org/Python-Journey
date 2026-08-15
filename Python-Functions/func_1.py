def  func_1(x):
    def func_2():
        x = 'abc'
    x = x+1
    print(' in func_1(x): x = ',x)
    func_2()
    return x

x = 3
z = func_1(x)