def func_1():
    """
    Returing a function
    """
    def x(a,b):
        return a+b
    return x # Yaah pr x func ko call kr rahi he

val = func_1()(3,4)
print(val)