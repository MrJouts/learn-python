burguers = {
    "Big Mac": {
        "ingredientes": ["hamburguesa", "pepino", "lechuga", "mayonesa"],
        "precio": 140,
        "descuento": "miércoles",
    },
    "Cuarto de libra": {
        "ingredientes": ["hamburguesa grande", "queso", "ketchup", "cebolla"],
        "precio": 170,
        "descuento": "jueves",
    },
    "Mac Pollo": {
        "ingredientes": ["hamburguesa de pollo", "queso", "lechuga", "cebolla"],
        "precio": 130,
        "descuento": "lunes",
    },
}

for hamburguesa, detalles in burguers.items():
    print(
        hamburguesa.title()
        + ": $"
        + str(detalles["precio"])
        + " | Descuento: "
        + detalles["descuento"].capitalize()
    )
    for ingrediente in detalles["ingredientes"]:
        print("\t" + ingrediente.title())
