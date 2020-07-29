print("Enter q to quit\n")

while True:
    try:
        x = input("Give me a number: ")
        if x == "q":
            break
        x = int(x)

        y = input("Give me another number: ")
        if y == "q":
            break
        y = int(y)

    except ValueError:
        print("Not number provided")

    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum))
