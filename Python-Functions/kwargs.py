def display(**kwargs):

    for (key,value) in kwargs.items():
        print(key,'->',value)

print(display(india='delhi',pakistan='islamabad'))