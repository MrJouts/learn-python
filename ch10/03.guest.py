user_name = input("What's your name?")
filename = "ch10/guest.txt"

with open(filename, "w") as file_object:
    file_object.write(user_name)
    print(user_name + " registered on the Data Base")

