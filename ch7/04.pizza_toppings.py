prompt = "Please, enter a topping: "
topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print(topping.capitalize() + " added to your pizza.")

