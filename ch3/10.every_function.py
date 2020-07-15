# List

destinations = ["Buenos Aires", "New York", "Tokyo", "Mallorca"]

print("Lista orginal:\n" + str(destinations))

# Nuevo destino al final
destinations.append("Bogotá")
print("Agrego Bogotá:\n" + str(destinations))

# Nuevo destino en el medio
destinations.insert(1, "San Francisco")
print("Visito San francisco antes que New York:\n" + str(destinations))

# Remuevo un detino
del destinations[4]
print("No voy a visitar Mallorca:\n" + str(destinations))

# Remuevo otro destino
place = destinations.pop(3)
print("Voy a visitar " + str(place) + " en otro viaje:\n" + str(destinations))

# Remuevo otro destino
place = destinations.remove("Bogotá")
print("No voy a visitar Bogotá:\n" + str(destinations))

# Ordeno los destinos
destinations.sort()
print("Ordeno los destinos:\n" + str(destinations))

# Ordeno los destinos al revés
destinations.sort(reverse=True)
print("Ordeno los destinos al revés:\n" + str(destinations))

# Ordeno los destinos
print("Ordeno los destinos nuevamente:\n" + str(sorted(destinations)))
print("Listado original: " + str(destinations))

# Ordeno los destinos al revés
print("Ordeno los destinos nuevamente:\n" + str(sorted(destinations, reverse=True)))
print("Listado original: " + str(destinations))

# Invierto el orden
destinations.reverse()
print("Ordeno los destinos al revés:\n" + str(destinations))

# Length
print("Cantidad de lugares que voy a visitar: " + str(len(destinations)))