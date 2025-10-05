# CSV file handling

import pandas as pd

# Writing to CSV
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
df.to_csv("people.csv", index=False)  # index=False to avoid writing row numbers to file
print("Data written to people.csv")

# Reading from CSV
df = pd.read_csv("people.csv")
print("Data read from people.csv:")
print(df)



# converting api data (JSON) to CSV
import requests

# Example API
import requests
import pandas as pd
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()   # JSON list of dicts

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("api_users.csv", index=False)
print("API data saved to CSV")

# Reading back the CSV
df = pd.read_csv("api_users.csv")
print("Data read from api_users.csv:")
print(df)
