cities = {
    "buenos aires": {
        "country": "argentina",
        "population": 40000000,
        "fact": "Ciudad de pobres corazones",
    },
    "akihabara": {
        "country": "japón",
        "population": 36000000,
        "fact": "capitál del anime y la tecnología",
    },
    "paris": {
        "country": "Francia",
        "population": 14000000,
        "fact": "ciudad de las luces",
    },
}

for key, value in cities.items():
    print(
        key.title()
        + ": "
        + value["country"].title()
        + " / "
        + str(value["population"])
        + " / "
        + value["fact"].capitalize()
    )
