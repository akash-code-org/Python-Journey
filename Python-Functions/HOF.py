def square(x):
    return x**2
def transform(f,L):
    output = []
    for i in L:
        output.append(f(i))

    print(output)

L = [1,2,3,4]
print(transform(lambda x:x**2,L))