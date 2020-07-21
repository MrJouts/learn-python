favourite_places = {
    "flor": ["casa", "buenos aires", "new york"],
    "Brenda": ["san francisco", "Brazil", "Noruega", "Italia"],
    "marcos": ["tokyo", "Francia",],
}

for friend, places in favourite_places.items():
    print(friend)
    for place in places:
        print("\t" + place)
