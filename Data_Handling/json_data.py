'''

| Function  | Input              | Output      | Works on | Use Case      |
| --------- | ------------------ | ----------- | -------- | ------------- |
| `load()`  | File object (JSON) | Python obj  | File     | File → Dict   |
| `loads()` | JSON string        | Python obj  | String   | String → Dict |
| `dump()`  | Python obj + file  | Writes file | File     | Dict → File   |
| `dumps()` | Python obj         | JSON string | String   | Dict → String |


File → load / dump
String → loads / dumps



| Feature            | `json.load()`                   | `json.loads()`                |
| ------------------ | ------------------------------- | ----------------------------- |
| Input Type         | File object (opened file)       | JSON string                   |
| Typical Usage      | Read JSON directly from a file  | Parse API/DB string to Python |
| Real-world Example | Config file, local JSON dataset | REST API response, DB storage |

'''

# JSON load and loads


'''

json.load(file_object)
Input → A file object (that contains JSON data).
Use case → When you already have a .json file and you want to convert it into a Python dictionary or list.
Output → A Python object (dict/list).


example of file object: data.json
{
  "id": 101,
  "name": "Ratan Sharma",
  "skills": ["Python", "FastAPI", "Docker"],
  "department": {
    "name": "AI/ML",
    "projects": ["ETL Pipeline", "LLM Fine-tuning"]
  }
}

'''

import json

# Open and load JSON file
path = r"data1.json"
# with open("Data_Handling/data1.json", "r") as file:
with open("Data_Handling/data1.json", "r") as file:
  data = json.load(file)

# Now 'data' is a Python dictionary
print(type(data))   # <class 'dict'>

# Access values
print(data["name"])                     # Ratan Sharma
print(data["skills"][1])                # FastAPI
print(data["department"]["projects"][0])  # ETL Pipeline



# JSON loads
'''
json.loads(string_data)
Input → A string containing JSON data.
Use case → When JSON comes as a string (for example, from an API response, database, or Redis) and you want to convert it into a Python dictionary or list.
Output → A Python object (usually a dict or list).

'''

# single-line JSON string
json_string = '{"name": "Ratan", "age": 25, "skills": ["Python", "FastAPI"]}'


# multi-line JSON string
json_string12 = '''
{
  "id": 102,
  "name": "Anita Verma",
  "skills": ["JavaScript", "React", "Node.js"],
  "department": {
    "name": "Frontend",
    "projects": ["Website Revamp", "Mobile App"]
  }
}
'''

# Nested objects → Python lists and dictionaries
json_string1 = '''[
{
  "id": 102,
  "name": "Anita Verma",
  "skills": ["JavaScript", "React", "Node.js"],
  "department": {
    "name": "Frontend",
    "projects": ["Website Revamp", "Mobile App"]
  }
}
]'''


# loads the JSON string into a Python object
data1 = json.loads(json_string12)
data2 = json.loads(json_string1)
print(type(data1))  # <class 'dict'>
print(type(data2))  # <class 'list'>

# Access values
print(data1["name"])                     # Anita Verma
print(data1["skills"][0])                # JavaScript
print(data1["department"]["projects"][1])  # Mobile App