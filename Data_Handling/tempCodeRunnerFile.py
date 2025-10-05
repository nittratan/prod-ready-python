import json

# Open and load JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Now 'data' is a Python dictionary
print(type(data))   # <class 'dict'>

# Access values
print(data["name"])                     # Ratan Sharma
print(data["skills"][1])                # FastAPI
print(data["department"]["projects"][0])  # ETL Pipeline