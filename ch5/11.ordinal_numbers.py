ordinals = []

for number in range(1, 10):
    if number == 1:
        ordinals.append(str(number) + "st")
    elif number == 2:
        ordinals.append(str(number) + "nd")
    elif number == 3:
        ordinals.append(str(number) + "rd")
    else:
        ordinals.append(str(number) + "th")

print(ordinals)

