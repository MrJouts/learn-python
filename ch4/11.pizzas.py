pizzas = ["Pepperoni", "Provolone", "Napo"]

friend_pizzas = pizzas[:]

pizzas.append("Jamón y morrones")
friend_pizzas.append('Anchoas')

# print(pizzas)
# print(friend_pizzas)

print("--- My pizzas:")
for pizza in pizzas:
  print(pizza)

print("--- Friend pizzas")
for pizza in friend_pizzas:
  print(pizza)

