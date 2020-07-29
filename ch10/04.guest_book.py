message = "Hello Sir, What's your name? (q to quit)"
filename = "ch10/guest_book.txt"

while True:
    name = input(message)
    if name == "q":
        break
    with open(filename, "a") as file_object:
        file_object.write(name + "\n")
        print(name + ", Welcome to the Astoria")

