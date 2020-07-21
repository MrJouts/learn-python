pet_1 = {"Lola": {"type": "dog", "owner": "Emiliano"}}
pet_2 = {"Tommy": {"type": "parrot", "owner": "Belén"}}
pet_3 = {"Copito": {"type": "cat", "owner": "Marcelo"}}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for name, data in pet.items():
        print(name)
        print("\t" + data["type"] + " / " + data["owner"])

