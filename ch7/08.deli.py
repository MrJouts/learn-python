sandwich_orders = [
    "Árabe de JyQ",
    "Pebete completo",
    "Mila con lechuga y tomate",
    "Triple de miga JyQ",
]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("I made your " + sandwich)

print("\nFinished sandwiches:")
for finished in finished_sandwiches:
    print(finished)
