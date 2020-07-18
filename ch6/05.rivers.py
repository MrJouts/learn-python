rivers = {
    "nile": "egypt",
    "amazonas": "sudamerica",
    "danubio": "unión europea",
    "volga": "moscú",
    "ebro": "españa",
    "mississippi": "nueva orleans",
}

for river, city in rivers.items():
    print("The " + str(river.title()) + " runs through " + str(city.title()))

for river in rivers.keys():
    print("River: " + str(river.title()))

for city in rivers.values():
    print("City: " + city.title())
