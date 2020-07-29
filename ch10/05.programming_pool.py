message = "Why you like programming? (q to quit) \n"
filename = "ch10/programming_pool.txt"

while True:
    reason = input(message)

    if reason == "q":
        break

    with open(filename, "a") as f:
        f.write(reason + "\n")
        print("Woooow! that's a very good reason!")
