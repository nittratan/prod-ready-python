# Example of unhandled exception leading to program crash
print("Program started")

# Trying to open a file that may not exist
file = open("data.txt", "r")   # ❌ if file not found, program crashes
content = file.read()

print("File content:\n", content)
file.close()

print("Program ended")

# Example of handled exception allowing program to continue
print("\nProgram started with exception handling")

print("Program started")

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError as e:
    print("Error: File not found!", e)
except PermissionError as e:
    print("Error: No permission to read the file!", e)
except Exception as e:
    print(f"Unexpected error: {type(e).__name__} - {e}")
else:
    print("File content:\n", content)
    file.close()
finally:
    print("Program ended (cleanup done)")

# -------------------------------------------------------------------

def file_operations(filename):
    try:
        file = open(filename, "r")
        content = file.read()
    except FileNotFoundError as e:
        print("Error: File not found!", e)
    except PermissionError as e:
        print("Error: No permission to read the file!", e)
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__} - {e}")
    else:
        print("File content:\n", content)
        file.close()
    finally:
        print("Program ended (cleanup done)")

file_operations("data.txt")
print("This will run no matter what...")


# -------------------------------------------------------------------

# Prod-Level Best Practice → with statement (Auto close)
import logging

logging.basicConfig(level=logging.INFO)

print("Program started")

try:
    with open("data.txt", "r") as file:   # file auto-close hoga
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    logging.error("File does not exist.")
except Exception as e:
    logging.error("Unexpected error occurred", exc_info=True)
finally:
    print("Program ended")
print("This will run no matter what...")