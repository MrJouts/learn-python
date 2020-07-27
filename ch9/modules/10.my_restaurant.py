from restaurant import Restaurant, IceCreamStand

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

griddo = IceCreamStand("Griddo", "heladeria")
griddo.describe_restaurant()
griddo.show_flavors()

