def test(x):
    """" In this program we introduced global and local variables
    """ 
    print(x) # same variable
    print(x+1)

x = 5 # same variable
test(x)
print(x)

# Main program aur function ke under global aur local variable ke naam same rikkh sakti he