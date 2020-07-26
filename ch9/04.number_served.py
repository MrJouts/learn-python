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


restaurant = Restaurant("Lo de Charly", "parrilla")

restaurant.describe_restaurant()
restaurant.open()

print(restaurant.number_served)
restaurant.number_served = 30
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(15)
print(restaurant.number_served)

