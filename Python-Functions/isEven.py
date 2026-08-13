def is_even(num):
    """ Ye code even odd number check krta he
    """ # It is a docstring
    if num%2==0:
        return 'Even'
    else:
        return 'Odd'

print(is_even(3))
print(is_even.__doc__) # accessing docstring