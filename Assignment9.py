"""
Q1. In Python 3.X, what are the names and functions of string object types?

Ans-1. In Python 3.X, there are three main string object types:

str: This is the standard string type in Python. It represents a sequence of Unicode
characters and supports various string manipulation operations and methods.

bytes: This type represents a sequence of bytes. Unlike the str type, which stores Unicode
characters, bytes stores raw binary data. It is useful for handling data that is not intended
to be interpreted as text, such as images or network packets.

bytearray: This is similar to the bytes type, but it is mutable. It allows you to modify
the individual bytes within the sequence.

Q2. How do the string forms in Python 3.X vary in terms of operations?

Ans-2. The different string forms in Python 3.X vary in terms of the operations they support:

str objects support a wide range of string operations, such as concatenation, slicing, searching,
replacing, formatting, and more. They are immutable, meaning that once created, they cannot be modified in place.

bytes objects support operations specific to binary data, such as indexing, slicing, and methods for
working with binary data, like decode() and encode(). They are also immutable.

bytearray objects, like bytes, support operations for working with binary data, but they are mutable.
They can be modified in place, allowing you to change individual bytes within the sequence.

Q3. In 3.X, how do you put non-ASCII Unicode characters in a string?

Ans-3. In Python 3.X, you can include non-ASCII Unicode characters in a string by using Unicode escape
sequences or by directly including the characters using the appropriate encoding.

Unicode escape sequences: Non-ASCII Unicode characters can be represented using escape sequences in the
form \uXXXX or \UXXXXXXXX, where XXXX or XXXXXXXX represents the Unicode code point in hexadecimal.

Q4. In Python 3.X, what are the key differences between text-mode and binary-mode files?

Ans-4. The key differences between text-mode and binary-mode files in Python 3.X are:

Text-mode files (open() with default mode or mode set to "r", "w", or "a") handle the file content as
a sequence of Unicode strings. Python automatically performs character encoding and decoding based on
the default system encoding or the specified encoding.

Binary-mode files (open() with mode set to "rb", "wb", or "ab") handle the file content as a sequence 
of bytes. They allow you to read and write raw binary data without any encoding or decoding.

Text-mode files are suitable for handling text files where character encoding matters, while binary-mode
files are useful for working with non-text data, such as images or binary file formats.

Q5. How can you interpret a Unicode text file containing text encoded in a different encoding than your platform's default?

Ans-5. To interpret a Unicode text file containing text encoded in a different encoding than your platform's default, you can use the encoding parameter of the open() function or the encoding argument of the str object's decode() method.
"""
