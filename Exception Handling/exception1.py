# example of without exception handling

def divide_numbers(num1, num2):
    print("function started...")

    result = num1 / num2   # if Error here
    print("Division result is:", result)   # ❌ will not run
    print("Program ended")                 # ❌ will not run
    return result


divide_numbers(10, 0)   # ZeroDivisionError: division by zero
print("After function call...")   # ❌ will not run


# with exception handling
def divide_numbers_handled(num1, num2):
    print("function started...")
    # result = None
    try:
        # local variable 'result' created only if no error
        result = num1 / num2   # <-- If this fails, 'result' is never created
    except Exception as e:
        print(f"Error occurred while dividing {e}")
    return result

divide_numbers_handled(10, 0)   # ZeroDivisionError: division by zero
print("After function call...")   # ✅ will run


print("Program started")

try:
    x = 10 / 0
except ValueError:
    print("Handled ValueError")
finally:
    print("Finally block always runs")

print("Program ended")   # Will NOT run




# -------------------------------------------------------------------
# Exception and Traceback

'''
Without try-except: Python automatically raises the error → it displays the full traceback.
With try-except: The error is caught → the interpreter does not need to crash, so the traceback is suppressed by default.
If we want the traceback: we can manually use traceback.print_exc() or logging.exception() to display or log it.

'''
# try except does not give traceback
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Handled ZeroDivisionError")
print("Program ended")   # Will run


# Unhandled exception gives traceback and crashes program
print("Program started")
x = 10 / 0   # ZeroDivisionError: division by zero
print("Program ended")   # Will NOT run


# to add traceback even with try except
import traceback
print("Program started")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Handled ZeroDivisionError")
    traceback.print_exc()   # prints the traceback
print("Program ended")   # Will run

# format.exc() returns string
import traceback
print("Program started")
try:
    x = 10 / 0  # ZeroDivisionError: division by zero   
except ZeroDivisionError:
    print("Handled ZeroDivisionError")
    error_message = traceback.format_exc()   # returns the traceback as string
    print("Error message as string:\n", error_message)
print("Program ended")   # Will run