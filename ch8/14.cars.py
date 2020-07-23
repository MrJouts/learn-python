def make_car(manufacturer, model, **data):
    """Build a car with random data"""
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model
    for index, value in data.items():
        car[index] = value

    return car

car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)

