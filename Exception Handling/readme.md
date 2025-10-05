'''
1. Exception Handling in Python
Exception handling is the process of managing runtime errors in a program, 
ensuring that the application does not crash unexpectedly and can continue executing gracefully with 
proper error messages or corrective actions.


2. Root Level Concepts
try block → The section of code where exceptions are anticipated and monitored.
except block → The block that handles and responds to an exception when it occurs.
else block → Executes only if no exceptions are raised in the try block.
finally block → Executes regardless of whether an exception occurs, often used for cleanup tasks (e.g., closing a database connection).
raise → Used to explicitly trigger an exception in the program.
Custom Exceptions → User-defined exception classes created by inheriting from the built-in Exception class, enabling application-specific error handling.


3. Production Use-Cases
API failure → Handle failed API requests by retrying and logging the error details.
Database connection error → Rollback incomplete transactions and generate alerts for monitoring.
File I/O issue → Safely handle missing or corrupted files to prevent application crashes.
Validation error → Raise custom exceptions with descriptive messages for invalid inputs.
Centralized error handling → Implement global exception handling mechanisms (e.g., middleware in FastAPI/Django) to ensure consistent error responses across the application.

'''


