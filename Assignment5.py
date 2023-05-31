"""
Q1. What is the meaning of multiple inheritance?
Ans- Multiple inheritance is a feature of object-oriented programming where a class can inherit
attributes and methods from multiple parent classes. This means that a subclass can have more
than one superclass. In multiple inheritance, the subclass inherits the characteristics of all
its parent classes, allowing it to have a combination of behaviors from different sources.

Q2. What is the concept of delegation?
Ans- Delegation is a design pattern in which an object forwards a specific task or responsibility
to another object, known as a delegate. Instead of implementing the task itself, the delegating
object assigns the responsibility to the delegate object. This promotes code reusability and allows
for dynamic behavior by allowing different delegate objects to handle the task differently.

Q3. What is the concept of composition?
Ans- Composition is a design principle where complex objects are built by combining simpler objects
or components. It involves creating an object that contains other objects as part of its internal
structure. The composed object can then utilize the functionality of its component objects to achieve
its own behavior. Composition promotes code reuse, modularity, and flexibility.

Q4. What are bound methods and how do we use them?
Ans- Bound methods are methods that are associated with an instance of a class. When a method is
accessed through an instance, it automatically receives the instance as the first argument (self).
This binding process is handled by the Python runtime and allows methods to access the instance's
attributes and perform actions specific to that instance. Bound methods are commonly used to operate
on instance data and provide behavior that depends on the specific instance.

Q5. What is the purpose of pseudoprivate attributes?
Ans- Pseudoprivate attributes in Python are attributes that are prefixed with a double underscore
(e.g., __attribute). These attributes are intended to be treated as private and are subject to name
mangling, where the attribute name is modified to avoid clashes with subclasses. The purpose of
pseudoprivate attributes is to provide a level of name protection and to indicate that the attribute
is intended for internal use within the class, discouraging direct access from outside the class.

"""
