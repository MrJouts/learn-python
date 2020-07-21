active = True
while active:
    topping = input("Please, enter a topping: ")
    if topping == "quit":
        break
    print(topping.capitalize() + " added to your pizza.")

