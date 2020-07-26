class Restaurant:
    """Just a new restaurant in town"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name an cuisine_type atributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(self.restaurant_name.capitalize() + " (" + self.cuisine_type + ")")

    def open(self):
        """Simulate opening"""
        print(self.restaurant_name.capitalize() + " is now open!")


restaurant = Restaurant("Lo de Charly", "parrilla")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open()

restaurant_luigi = Restaurant("Lugi's Manssion", "Italian cuisine")
restaurant_sushi = Restaurant("Itamae sushi", "Oriental food")

restaurant_luigi.describe_restaurant()
restaurant_luigi.open()
restaurant_sushi.describe_restaurant()
restaurant_sushi.open()
