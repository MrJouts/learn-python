users = ["king192", "jumpeikun", "admin", "jabba", "x_tsune_x"]

for user in users:
    if user == "admin":
        print("\nHello Admin, would you like to see a status report?\n")
    else:
        print("Hello " + str(user) + ", thank you for loggin again.")