vacations = {}

active = True
while active:
    # Pregunto por nombre y vacaciones
    user = input("Como te llamás?\n")
    vacacion = input("Como serían tus vacaciones soñadas?\n")

    # Agrego la vacación a la lista
    vacations[user] = vacacion

    # Pregunto si desea ingresar otra persona
    respuesta = input("Querés ingresar otra persona? (si/no)\n")
    if respuesta == "no":
        active = False

# Listado de vacaciones
for user, vacacion in vacations.items():
    print(user.title() + ": " + vacacion.capitalize())

