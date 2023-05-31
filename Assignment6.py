"""
Q1. Describe three applications for exception processing.

Ans 1. Three applications for exception processing are:

Error Handling: Exception processing is commonly used for error handling in software applications.
When an error occurs during program execution, an exception is raised, allowing the program to
handle the error gracefully. Exception processing enables developers to catch and handle errors,
provide meaningful error messages, and take appropriate actions to recover from the error.

Input Validation: Exception processing is useful for validating user input in applications.
By using exceptions, you can catch and handle invalid input or unexpected data entered by the
user. For example, if a user enters a non-numeric value in a field that expects a number, an
exception can be raised to notify the user and prompt them to enter valid input.

Resource Management: Exception processing is employed for managing system resources effectively.
For instance, when working with file I/O operations, exceptions can be used to handle cases where 
files cannot be accessed or when unexpected errors occur during file manipulation. By properly
handling exceptions, resources can be released, ensuring the system remains in a stable state.

Q2. What happens if you don't do something extra to treat an exception?

Ans 2. If you don't handle an exception properly, it will result in an unhandled exception,
which can lead to program termination or unexpected behavior. When an unhandled exception
occurs, the program may crash, display an error message to the user, or enter an undefined state.
This can have negative consequences, such as data loss, instability, or an unsatisfactory user experience.

Q3. What are your options for recovering from an exception in your script?

Ans 3. When recovering from an exception in your script, you have several options:

Exception Handling: You can use try-except blocks to catch and handle specific exceptions.
By enclosing the code that may raise an exception within a try block, you can handle the
exception using one or more except blocks, which specify the actions to be taken when a
particular exception occurs. This allows you to recover from the exception gracefully and
continue program execution.

Exception Propagation: If you cannot handle the exception at the current level, you can choose
to let the exception propagate up the call stack. This means allowing the exception to be passed
to higher-level functions or to the main program, where it can be caught and handled appropriately.

Q4. Describe two methods for triggering exceptions in your script.

Ans 4. Two methods for triggering exceptions in your script are:

Raise Statement: You can explicitly raise an exception using the raise statement. This allows you
to generate an exception at a specific point in your code. You can specify the type of exception
to be raised, along with an optional error message or additional information.

Built-in Exceptions: Python provides a set of built-in exceptions that can be raised to indicate
specific types of errors or exceptional conditions. For example, you can raise a ValueError when
invalid input is detected or an IndexError when accessing a list with an out-of-range index. By
raising these exceptions, you can communicate the specific nature of the error to the calling code
or handle it using appropriate exception handling mechanisms.

Q5. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists.

Ans 5. Two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists, are:

Finally Block: You can use a finally block in conjunction with a try-except block. The code within the
finally block is executed regardless of whether an exception occurred or not. This allows you to specify
cleanup or termination code that should be executed regardless of the outcome. The finally block is commonly
used to release resources, close files, or perform other essential cleanup tasks.

Context Managers: Python provides a context manager protocol that allows you to define objects that define the
__enter__ and __exit__ methods. The __exit__ method is executed at the end of the code block, whether an exception
occurred or not. Context managers are commonly used with the with statement and ensure that any resources associated
with the object are properly released or cleaned up, regardless of exceptions.

"""
