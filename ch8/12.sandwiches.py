def make_sandwitch(*toppings):
    """Make sandwich whit variable toppings"""
    print("Your sandwich will have the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_sandwitch("jamón", "queso", "tomate")
make_sandwitch("peperoni", "mostaza", "gruyere")
make_sandwitch("pavita", "cheddar", "mayonesa")

