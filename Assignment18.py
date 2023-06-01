"""

Q1. Describe the differences between text and binary files in a single paragraph.

Text files and binary files differ in how they store and represent data. Text files store data
as human-readable characters encoded in a specific character encoding, such as ASCII or UTF-8.
They typically contain plain text data, such as documents, scripts, or configuration files. 
Binary files, on the other hand, store data in a format that is not directly human-readable. 
They can contain any type of data, including images, audio, video, or serialized objects. Binary
files store data in their raw binary representation, which is not tied to any specific character encoding.

Q2. What are some scenarios where using text files will be the better option? When would you like to use
binary files instead of text files?

Text files are often a better option when the data is primarily composed of human-readable text, such as
documents, logs, or configuration files. Text files can be easily created, edited, and viewed using a text
editor. They are suitable for storing data that needs to be readable and editable by humans. On the other
hand, binary files are useful when working with non-textual data, such as multimedia files or serialized
objects. Binary files preserve the raw binary representation of the data, allowing for efficient
storage and processing of complex data structures.

Q3. What are some of the issues with using binary operations to read and write a Python integer directly to disk?

When using binary operations to read and write a Python integer directly to disk, some issues may arise.
One issue is that the binary representation of integers can vary depending on the platform's byte order 
(big-endian or little-endian). If the binary file is written on a system with a different byte order than 
the one reading it, the integer values may be interpreted incorrectly. Another issue is that binary files
are not human-readable, making it challenging to inspect and modify the data directly. Additionally, there
is no automatic encoding/decoding of characters in binary files, so special considerations need to be
taken if dealing with text data.

Q4. Describe a benefit of using the with keyword instead of explicitly opening a file.

The benefit of using the with keyword instead of explicitly opening a file is that it automatically takes
care of resource management. When a file is opened using with, it ensures that the file is properly closed,
even if an exception occurs within the with block. This helps prevent resource leaks and ensures the file
is released in a timely manner. The with statement provides a cleaner and more concise way to work with
files, eliminating the need for explicit calls to file.close().

Q5. Does Python have the trailing newline while reading a line of text? Does Python append a newline when you
 write a line of text?

When reading a line of text using Python, it includes the trailing newline character (\n) in the returned string,
if it exists in the file. Python does not strip the newline character by default. However, you can use the
rstrip() method to remove trailing whitespace characters, including the newline character.

When writing a line of text using Python, by default, Python does not append a newline character (\n) at the
end of the written line. It is the responsibility of the programmer to explicitly add the newline character
if desired. This behavior allows for more flexibility in controlling line breaks when writing to a file.

Q6. What are some examples of how to use the match object returned by re.match and re.search?

The match object returned by re.match and re.search provides various methods and attributes to access 
information about the matched pattern. Some examples of using the match object include:

Using the group() method to retrieve the entire matched substring.
Using the start() and end() methods to get the starting and ending indices of the match.
Using named groups to access specific parts of the match using the group('name') method.
Using the span() method to retrieve the starting and ending indices as a tuple.
Checking if a match was found using the bool() function on the match object.
Q7. What is the difference between using a vertical bar (|) as an alteration and using square brackets as 
a character set?

In regular expressions, a vertical bar (|) is used as an alteration or logical OR operator. It allows you
to specify multiple alternative patterns, and the regular expression engine will try to match any of those
patterns. For example, the pattern "cat|dog" would match either "cat" or "dog".

On the other hand, square brackets ([]) are used to define a character set or character class. Inside the
square brackets, you can list individual characters or ranges of characters. The regular expression engine
will try to match any one character from the defined set. For example, the pattern "[aeiou]" would match
any vowel character.

Q8. Can you identify repeated items within a target string using named groups, as in "The cow jumped over the moon"?

Yes, you can identify repeated items within a target string using named groups in regular expressions. By
using the syntax "(?P<name>pattern)", you can define a named group in the regular expression pattern. 
This allows you to extract and reference the matched substring using the specified name. In the given
example, you can define a pattern to match repeated words using a named group, such as 
"(?P<word>\w+)\s+(?P=word)". This would match and capture repeated words within the target string.

Q9. When parsing a string, what is at least one thing that the Scanner interface does for you that the
 re.findall feature does not?

The Scanner interface provides advanced parsing capabilities that go beyond what the re.findall() function
offers. One thing the Scanner interface does is allow you to tokenize a string by defining custom patterns
for different types of tokens. It enables you to iterate over the tokens one by one, rather than returning
all matches at once like re.findall(). Additionally, the Scanner interface provides methods for skipping
specific patterns or ignoring whitespace, making it easier to extract meaningful information from the
input string.

Q10. Does a scanner object have to be named scanner?

No, a scanner object does not have to be named "scanner". The choice of variable name for the scanner object
is up to the programmer. It is common to use intuitive and descriptive variable names that reflect the 
purpose of the scanner object. The name "scanner" is often used as a convention, but it is not a requirement.
As long as the variable name is valid and follows the naming rules of the programming language, any name 
can be used for the scanner object.
"""