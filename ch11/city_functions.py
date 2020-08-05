def get_full_city(city, country, population=""):
    message = city.title() + ", " + country.title()
    if population:
        message += " - population " + str(population)
    return message

