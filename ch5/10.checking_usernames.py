current_users = ["king192", "jumpeikun", "admin", "jabba", "x_tsune_x"]
new_users = ["kariota", "Jabba", "ro_cio", "JumpeiKun", "Julibaba"]

for user in new_users:
    if user.lower() in current_users:
        print("Username " + str(user) + " not avilable. Pelase, enter a new one.")
    else:
        print(str(user) + " is available.")
