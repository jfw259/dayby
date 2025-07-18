i=0
while i<3:
    user_name = input("Enter your name: ")
    user_password = input("Enter your password: ")
    if user_name=='3464574841' and user_password=='jfwaabbcc123':
       print("Login successful")
       i=3
    else:
        if i<3:
            print("Login failed, please try again")
            i=i+1
else:
    print('gun')

