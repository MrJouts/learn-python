import json

filename = "favorite.json"

try:
    with open(filename) as f:
        number = json.load(f)
        print("I know yor favorite number, It's: " + str(number))
except FileNotFoundError:
    number = input("What's yor favorite number? ")
    with open(filename, "w") as f:
        json.dump(number, f)
        print("...done!")
