def multiply(*args):
    product  = 1

    for i in args:
        product*=i

    print(args) # args values ko tuple mein store krta he
    print(product)

print(multiply(2,2,2,2))