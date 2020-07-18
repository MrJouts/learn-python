users = []

if users:
    for user in users:
        if user == "admin":
            print("Hello Admin, would you like to see a status report?")
        else:
            print("Hello " + str(user) + ", thank you for loggin again.")
else:
    print("We need to find some users!")
