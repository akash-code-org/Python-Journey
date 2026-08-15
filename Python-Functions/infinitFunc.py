def func_1():
    """ output will be infinit
    """
    def func_2():
        print('Inside 2')
        func_1()
    func_2()
    print('Inside 1')

func_1()