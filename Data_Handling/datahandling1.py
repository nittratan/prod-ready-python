# Handling files in Python
# Writing into a file
f = open("sample.txt", "w")   # "w" → write mode (overwrites if file exists)
f.write("Hello, this is a text file.\n")
f.write("Second line of data.\n")
f.close()   # always close to avoid memory leaks

# Reading from a file
f = open("sample.txt", "r")   # "r" → read mode
content = f.read()
print("File content:\n", content)
f.close()


# Appending to a file
f = open("sample.txt", "a")   # "a" → append mode
f.write("Appending a new line.\n")
f.close()


# automatic file handling using 'with' statement (context manager)
# Writing safely
with open("sample.txt", "w") as f:
    f.write("Safe write using context manager.\n")

# Reading safely
with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)


# reading line by line
with open("sample.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())   # strip() removes leading/trailing whitespace


# binary file handling
# Writing binary data
with open("binaryfile.bin", "wb") as f:   # "wb" → write binary mode
    f.write(b'\x00\xFF\x7A\x3C')   # writing raw bytes      

data = b"Hello in binary!\n"

with open("binary_file.bin", "wb") as f:   # "wb" → write binary
    f.write(data)


with open("binary_file.bin", "rb") as f:   # "rb" → read binary
    content = f.read()
    print("Binary content:", content)
    print("Decoded content:", content.decode('utf-8'))  # decode bytes to string


#  Object serialization with pickle
# Serialization = Convert Python object → byte stream (store in file)
# Deserialization = Convert byte stream → Python object

import pickle

data = {"name": "Ratan", "age": 25, "skills": ["Python", "FastAPI"]}

# Serialize (dump object into file)
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Deserialize (load back object from file)
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print("Original:", data)
print("Loaded from pickle:", loaded_data)



# tempfile module for temporary files
import tempfile, os

# Create temp file (not auto-deleted)
tmp = tempfile.NamedTemporaryFile(delete=False, mode="w+")
print("Temp file created at:", tmp.name)

tmp.write("Manual delete example.\n")
tmp.close()

# Later in code → manually delete
os.remove(tmp.name)
print("Temp file deleted manually.")