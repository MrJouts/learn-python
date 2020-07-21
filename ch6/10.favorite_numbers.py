favorite_numbers = {
    "carlos": [1, 22, 43],
    "brenda": [10],
    "emanuel": [2, 7, 400],
    "leticia": [7, 8],
    "mariana": [76, 1337],
}

for person, numbers in favorite_numbers.items():
    print(person + ": ")
    for number in numbers:
        print("\t" + str(number))

