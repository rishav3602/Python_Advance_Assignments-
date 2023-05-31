"""
Q1. What are the two latest user-defined exception constraints in Python 3.X?

Ans- 1. The two latest user-defined exception constraints in Python 3.X are:

Inheriting from the Exception class: User-defined exceptions should typically inherit from the built-in Exception class or one of its subclasses. This ensures that the custom exception class follows the standard exception hierarchy and provides the necessary attributes and methods.

Defining an appropriate error message: User-defined exceptions should include an error message that provides meaningful information about the exceptional condition or error that occurred. This allows users or developers to understand the cause of the exception and take appropriate actions.

Q2. How are class-based exceptions that have been raised matched to handlers?

Ans- 2. Class-based exceptions that have been raised are matched to handlers based on the exception's type hierarchy. When an exception is raised, Python searches for an appropriate exception handler by traversing the exception's inheritance hierarchy. The search starts with the most specific exception type and proceeds to more general types until a matching handler is found. If no suitable handler is found, the exception propagates up the call stack.

Q3. Describe two methods for attaching context information to exception artifacts.

Ans- 3. Two methods for attaching context information to exception artifacts are:

Exception arguments: When raising an exception, you can pass additional arguments that provide context information about the exceptional condition. These arguments can be accessed within the exception handler to gain insights into the cause of the exception.

Exception attributes: Custom exception classes can define attributes that hold relevant context information. These attributes can be set when the exception is raised and accessed within the exception handler to provide additional details about the error or exceptional condition.

Q4. Describe two methods for specifying the text of an exception object's error message.

Ans- 4. Two methods for specifying the text of an exception object's error message are:

Passing an error message as an argument: When raising a built-in or user-defined exception, you can pass an error message as an argument. This error message provides a textual description of the exception and helps in understanding the cause of the error.

Overriding the __str__() method: In custom exception classes, you can override the __str__() method to specify the text of the exception's error message. This method should return a string representation of the exception that includes relevant information about the error.

Q5. Why do you no longer use string-based exceptions?

Ans- 5. String-based exceptions are no longer used in modern Python because they have several limitations and drawbacks. Some reasons for not using string-based exceptions include:

Lack of hierarchy: String-based exceptions do not provide a hierarchical structure, making it difficult to categorize and handle exceptions based on their types.

Lack of functionality: String-based exceptions lack the functionality and behavior provided by class-based exceptions. Class-based exceptions allow for more robust error handling, traceback information, and customization.

Readability and maintainability: String-based exceptions can be less readable and harder to maintain. They often require manual string comparisons for error handling, making the code more error-prone and less expressive.

Inconsistency: String-based exceptions do not follow the standard exception hierarchy used by built-in exceptions, making it challenging to handle them consistently with the rest of the exception system.

By using class-based exceptions, Python provides a more structured and standardized approach to exception handling, enabling better code organization, error categorization, and overall robustness in error handling.

"""