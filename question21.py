import json

data = {"name" : "Rudra"}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json") as file:
    result = json.load(file)

print(result["name"])