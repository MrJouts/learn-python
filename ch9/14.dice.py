from random import randint


class Dice:
    """A regular dice"""

    def __init__(self, sides=6):
        """Initialize the side property"""
        self.sides = sides

    def show_sides(self):
        """Show the number of sides"""
        print("Sides: " + str(self.sides))

    def roll_die(self, times=1):
        """Prints a random number between 1 and the number of sides"""
        print("Rolled " + str(times) + " times !!")
        if times == 1:
            results = randint(1, self.sides)
        else:
            results = []
            for item in range(1, times):
                results.append(randint(1, self.sides))
        print("Results: " + str(results))


dice_6 = Dice()
dice_6.show_sides()
dice_6.roll_die(10)

dice_10 = Dice(10)
dice_10.show_sides()
dice_10.roll_die(10)

dice_20 = Dice(20)
dice_20.show_sides()
dice_20.roll_die(10)
