sandwich_orders = [
    "Árabe de JyQ",
    "pastrami",
    "Pebete completo",
    "pastrami",
    "Mila con lechuga y tomate",
    "Triple de miga JyQ",
    "pastrami",
]

finished_sandwiches = []

print("We run out pastrami! \n".upper())

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("I made your " + sandwich)

print("\nFinished sandwiches:")
for finished in finished_sandwiches:
    print(finished)
