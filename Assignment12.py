"""
Q1. Does assigning a value to a string's indexed character violate Python's string immutability?

Ans 1. Yes, assigning a value to a string's indexed character violates Python's string immutability.
Strings in Python are immutable, which means that once a string is created, its individual characters
cannot be modified. If you attempt to assign a new value to a specific indexed character of a string,
you will encounter a TypeError stating that 'str' object does not support item assignment.

Q2. Does using the += operator to concatenate strings violate Python's string immutability? Why or why not?

Ans 2. No, using the += operator to concatenate strings does not violate Python's string immutability.
The += operator performs string concatenation by creating a new string that combines the original string
and the appended string. Although a new string is created, the original strings remain unchanged. This
operation is different from modifying a specific indexed character, as it creates a new string object
rather than modifying the existing one.

Q3. In Python, how many different ways are there to index a character?

Ans 3. In Python, there is one primary way to index a character in a string, which is by using square
brackets [] with the index position of the desired character. For example, my_string[0] retrieves the
first character of the string.

Q4. What is the relationship between indexing and slicing?

Ans 4. Indexing and slicing are both used to access specific portions of a string in Python:

Indexing: Indexing is used to retrieve a single character at a specific position in a string. It uses
the square bracket notation with an index value inside, such as my_string[0] to access the first character.

Slicing: Slicing is used to retrieve a substring, which is a portion of a string that includes multiple
characters. It uses the colon : notation to specify a range of indices, such as my_string[1:4] to retrieve
characters from index 1 to index 3.

In summary, indexing is used to access a single character, while slicing is used to access a portion of a
string containing multiple characters.

Q5. What is an indexed character's exact data type? What is the data form of a slicing-generated substring?

Ans 5. In Python, an indexed character is of type str, which represents a single Unicode character.

A slicing-generated substring is also of type str, representing a sequence of Unicode characters. It behaves
like a regular string and can be assigned to variables or used as input for other string operations.

Q6. What is the relationship between string and character "types" in Python?

Ans 6. In Python, strings are sequences of characters. Each character within a string is represented as a Unicode
character. The "type" of a character within a string is the str type. The str type in Python represents a string
of Unicode characters, and each character is itself a str type.

Q7. Identify at least two operators and one method that allow you to combine one or more smaller strings to create
a larger string.

Ans 7. Two operators and one method that allow you to combine smaller strings into a larger string are:

Concatenation (+ operator): The + operator concatenates two or more strings, joining them together to create a larger
string. For example: result = string1 + string2.

String formatting (% operator or str.format() method): The % operator or the str.format() method allows you to insert
values into a string template. This enables you to combine strings with formatted values. For example:

Using % operator: result = "Hello, %s!" % name
Using str.format(): result = "Hello, {}!".format(name)
Joining (str.join() method): The str.join() method joins a sequence of strings into a single string, using
the original string as a separator. For example: result = '-'.join(['a', 'b', 'c']) would result in 'a-b-c'.

Q8. What is the benefit of first checking the target string with in or not in before using the index method to find a substring?

Ans 8. The benefit of first checking the target string with in or not in before using the index method is to avoid
raising a ValueError when the substring is not found in the target string.

By using the in or not in operators, you can check if a substring exists within a string without encountering an error.
If the substring is found, you can proceed to use the index method to find the exact position or index of the substring
within the target string. If the substring is not found, you can handle the absence of the substring gracefully without
causing the program to terminate abruptly.

Q9. Which operators and built-in string methods produce simple Boolean (true/false) results?

Ans 9. The following operators and built-in string methods produce simple Boolean (true/false) results:

Comparison operators: Comparison operators such as ==, !=, <, >, <=, and >= can be used to compare strings and
produce Boolean results. For example, "apple" == "banana" would evaluate to False.

in and not in operators: The in and not in operators are used to check if a substring exists within a string.
They return True if the substring is found and False otherwise. For example, "apple" in "pineapple" would evaluate to True.

startswith() and endswith() methods: The startswith() method is used to check if a string starts with a
specified prefix, while the endswith() method checks if a string ends with a specified suffix. Both methods
return a Boolean result. For example, "Hello".startswith("He") would evaluate to True.

isalpha(), isdigit(), isalnum(), isspace() methods: These methods are used to check the nature of the characters
in a string. They return True if the characters meet the specified criteria and False otherwise. For example,
"abc".isalpha() would evaluate to True.

"""
