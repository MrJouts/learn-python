guests = []
guests.append("Carla Conte")
guests.insert(0, "El Doctor")
guests.insert(2, "Paco Amoroso")
guests.append("C4tri3l")

guest_removed = guests.pop(1)
print(guest_removed + ", se canceló la fiesta")

guest_removed = guests.pop(1)
print(guest_removed + ", se canceló la fiesta")

del guests[0]
del guests[0]

print(guests)