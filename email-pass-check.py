email = input("enter your email: ")
password = input("enter your password: ")

if email == "youmail@gmail.com" and password == "youpassword":
    print("login successful")
elif email == "youmail@gmail.com" and password != "youpassword":
    print("invalid password")
    print("try again")
    password = input("enter your password: ")
    if password == "youpassword":
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid email or password")