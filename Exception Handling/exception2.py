# Try , Except , Finally

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")


# this will run no matter what error or not
print("This will run ...")


# raise Exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise Exception("Age must be at least 18.") # terminate execution of program
    else:
        print("Age is valid.")


check_age(19)
# this will not run if exception is raised
print("After check_age() function call...")