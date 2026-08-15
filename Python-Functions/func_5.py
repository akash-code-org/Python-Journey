def func_a():
    print('Inside func_a ')
def func_b(z):
    print('Inside func_c ')
    return z()

print(func_b(func_a))