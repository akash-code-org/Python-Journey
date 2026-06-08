email = input("Enter your email: ")
if '@' in email:
    password = input("Enter your password: ")
    if email == "akash@gmail.com" and password == "123":
        print("Welcome")
    elif email == "akash@gmail.com" and password != "123":
        print("Incorrect password")
        password = input("Enter password: ")
        if password == "123":
            print("Welcome: ")
        else:
            print("Still incorrect")
    else:
        print("Incorrect detail: ")
else:
    print("Email is incorrect: ")