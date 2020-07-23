def make_great(magicians):
    """Add great to magicians"""

    great_magicians = []

    while magicians:
        great_magician = magicians.pop() + " the Great"
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)


def show_magicians(magicians):
    """Show a list of magicians"""

    for magician in magicians:
        print(magician)


magicians = ["David Copperfield", "El Mago Black", "Emanuelle", "Jansenson"]

make_great(magicians)
show_magicians(magicians)
