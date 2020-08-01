import json

filename = "favorite.json"
with open(filename) as f_json:
    number = json.load(f_json)
    print("I know yor favorite number, It's: " + str(number))
