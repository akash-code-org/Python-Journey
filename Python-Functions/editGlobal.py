def test(y):
    """ Eys code mein global variable ko edit kr rahi hain
    """
    global x
    x+=1

x = 5
test(x)
print(x)
print(test.__doc__)