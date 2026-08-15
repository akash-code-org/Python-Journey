def func_1():
    def func_2():
        print('Inside function 1')
    func_2
    print('Inside function 2')

func_1()