person_1 = {
    "first_name": "Carlos",
    "last_name": "Gutierrez",
    "age": 45,
    "city": "Hamburgo",
}
person_2 = {
    "first_name": "María",
    "last_name": "Perez",
    "age": 27,
    "city": "Buenos Aires",
}
person_3 = {"first_name": "Takara", "last_name": "Matsuda", "age": 32, "city": "Tokyo"}
person_4 = {
    "first_name": "Joao",
    "last_name": "Verena",
    "age": 57,
    "city": "Porto Alegre",
}

people = [person_1, person_2, person_3, person_4]

for person in people:
    print(
        person["first_name"]
        + " "
        + person["last_name"]
        + ": "
        + str(person["age"])
        + " / "
        + person["city"]
    )
