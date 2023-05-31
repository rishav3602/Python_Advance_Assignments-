"""
Q1. Which two operator overloading methods can you use in your classes to support iteration?
Ans- To support iteration in your classes, you can use the __iter__ and __next__ methods.
The __iter__ method is responsible for returning the iterator object itself, and the
__next__ method is used to retrieve the next item from the iterator.

Q2. In what contexts do the two operator overloading methods manage printing?
Ans- The two operator overloading methods that manage printing are __str__ and __repr__.
The __str__ method is used to provide a human-readable string representation of the object,
typically for end-user consumption. The __repr__ method provides a more detailed string
representation that is primarily used for debugging and development purposes.

Q3. In a class, how do you intercept slice operations?
Ans- To intercept slice operations in a class, you can define the __getitem__ method.
This method allows instances of the class to support indexing and slicing operations.
When a slice is used on an instance of the class, the __getitem__ method is called
with the appropriate slice object.

Q4. In a class, how do you capture in-place addition?
Ans- To capture in-place addition in a class, you can define the __iadd__ method.
This method is called when the += operator is used on an instance of the class.
It allows you to define how the object should be modified when in-place addition is performed.

Q5. When is it appropriate to use operator overloading?
Ans- It is appropriate to use operator overloading when it makes the code more readable,
intuitive, and closely models the behavior of the objects being represented. Operator overloading
is especially useful when you want to provide custom behavior for operators that is specific to
the objects of your class. However, it should be used judiciously and in a way that does not lead 
to confusion or unexpected behavior.
"""
