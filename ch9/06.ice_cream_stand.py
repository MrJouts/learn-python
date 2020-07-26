class Restaurant:
    """Just a new restaurant in town"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name an cuisine_type atributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(self.restaurant_name.capitalize() + " (" + self.cuisine_type + ")")

    def open(self):
        """Simulate opening"""
        print(self.restaurant_name.capitalize() + " is now open!")

    def set_number_served(self, guests):
        self.number_served = guests

    def increment_number_served(self, newGuests):
        self.number_served += newGuests


class IceCreamStand(Restaurant):
    """Respresent a type of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["americana", "cereza", "chocolate", "banana split"]

    def show_flavors(self):
        """Display the available flavors"""
        print("Sabores: ")
        for flavor in self.flavors:
            print("\t" + flavor)


griddo = IceCreamStand("Griddo", "heladeria")
griddo.describe_restaurant()
griddo.show_flavors()
