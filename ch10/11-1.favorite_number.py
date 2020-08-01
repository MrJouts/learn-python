import json

favorite = input("What's yor favorite number?")
filename = "favorite.json"

with open(filename, "w") as f_json:
    json.dump(int(favorite), f_json)
