"""

Q1. Explain the difference between greedy and non-greedy syntax with visual terms in as few words as possible.
 What is the bare minimum effort required to transform a greedy pattern into a non-greedy one? What characters
   or characters can you introduce or change?

Ans - The greedy syntax in regular expressions matches as much as possible, while the non-greedy (also known as
 lazy or reluctant) syntax matches as little as possible. To transform a greedy pattern into a non-greedy one,
   you can introduce the question mark (?) character after the quantifier. For example, changing .* (greedy) to .*?
     (non-greedy).

Q2. When exactly does greedy versus non-greedy make a difference? What if you're looking for a non-greedy match
 but the only one available is greedy?

Ans - Greedy versus non-greedy makes a difference when the pattern includes a quantifier (such as *, +, ?, {n}, etc.)
 that can match multiple occurrences. Greedy matching will try to match as much as possible, potentially consuming
   more text than intended. If a non-greedy match is desired but only a greedy match is available, you can try to
     make the pattern more specific, use lookaheads, or use negated character classes to achieve the desired behavior.

Q3. In a simple match of a string, which looks only for one match and does not do any replacement, is the use
 of a nontagged group likely to make any practical difference?

Ans - In a simple match without any replacement, the use of a non-tagged group (a group without a capturing group
 number or a group name) may not make a practical difference in most cases. Non-tagged groups are typically used
   for grouping and logical grouping of subpatterns, but they do not affect the overall match result.

Q4. Describe a scenario in which using a nontagged category would have a significant impact on the program's outcomes.


Ans - One scenario where using a non-tagged category can have a significant impact is when using nested groups
 and backreferences. If you need to refer to a specific nested group using a backreference, the use of a 
 non-tagged group can change the numbering of the backreference and lead to incorrect results.

Q5. Unlike a normal regex pattern, a look-ahead condition does not consume the characters it examines. Describe
 a situation in which this could make a difference in the results of your program.

Ans - A situation where the non-consumptive nature of a look-ahead condition makes a difference is when you
 want to match a specific pattern only if it is followed by another pattern, without including the second
   pattern in the match. For example, if you want to match all occurrences of "apple" that are followed by 
   "pie" but do not include "pie" in the match, you can use a positive look-ahead assertion.

Q6. In standard expressions, what is the difference between positive look-ahead and negative look-ahead?

Ans - Positive look-ahead ((?=...)) asserts that the pattern inside the lookahead must be present for a match
 to occur, but it does not consume the characters. Negative look-ahead ((?!...)) asserts that the pattern 
 inside the lookahead must not be present for a match to occur. Both look-aheads do not include the characters
   of the lookahead in the overall match.

Q7. What is the benefit of referring to groups by name rather than by number in a standard expression?

Ans - Referring to groups by name in a standard expression provides better readability and maintainability 
of the regular expression. It makes the code more self-explanatory and reduces the chances of errors when 
the regex pattern is modified. Additionally, named groups allow you to access the matched text using meaningful 
names instead of relying on group numbers.

Q8. Can you identify repeated items within a target string using named groups, as in "The cow jumped over the moon"?
Ans - Yes, you can identify repeated items within a target string using named groups in regular expressions.
 Here's an example:


import re

pattern = r'(?P<animal>\w+)\s(?P<action>\w+)\s(?P<target>\w+)'
text = 'The cow jumped over the moon'

match = re.search(pattern, text)
if match:
    print(match.group('animal'))  # Output: cow
    print(match.group('action'))  # Output: jumped
    print(match.group('target'))  # Output: moon


Q9. When parsing a string, what is at least one thing that the Scanner interface does for you that the 
re.findall feature does not?
Ans - The Scanner interface provides a way to tokenize a string into meaningful components. It allows you
 to define specific patterns to match and extract tokens from the input string. One thing that the Scanner
   interface does for you, which re.findall does not, is that it provides a convenient way to iterate over
     the tokens one at a time, rather than returning all matches at once. This can be useful when you are 
     dealing with a large input string and want to process it incrementally.

Q10. Does a scanner object have to be named scanner?
Ans - No, a scanner object does not have to be named "scanner." The name given to the scanner object is
 simply a variable name chosen by the programmer and can be any valid variable name according to the programming
   language's syntax rules. The choice of variable name should be based on meaningful and descriptive naming 
   conventions to enhance code readability.

"""