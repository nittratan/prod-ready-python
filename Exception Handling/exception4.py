#  Custom error handling classe

class InvalidAgeError(Exception): # inherit from Exception class to create custom error 
    """Custom exception for invalid age inputs."""
    def __init__(self, age, message="Age must be between 18 and 60"):
        self.age = age
        self.message = message
        super().__init__(f"{message}. Given: {age}")


def validate_age(age):
    if age < 18 or age > 60:
        raise InvalidAgeError(age)
    else:
        print("Valid age:", age)


print("Program started")

try:
    validate_age(15)   # invalid case
    print("Age is valid")
except InvalidAgeError as e:
    print("Custom Error Caught:", e)
finally:
    print("Program ended")



# -------------------------------------------------------------------
class InsufficientBalanceError(Exception):
    """Raised when withdrawal exceeds account balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient balance. Current: {balance}, Tried: {amount}")


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(1000)

try:
    account.withdraw(1500)   # invalid withdrawal
except InsufficientBalanceError as e:
    print("Transaction Failed:", e)
else:
    print("Transaction Successful")
finally:
    print("Session Ended")
