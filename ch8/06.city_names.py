def city_country(name, country):
    return name.title() + ", " + country.title()


city = city_country("santiago", "chile")
print(city)

city = city_country("buenos aires", "argentina")
print(city)

city = city_country("paris", "Francia")
print(city)
