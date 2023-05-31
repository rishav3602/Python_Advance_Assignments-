"""
Q1. What is the purpose of Python&#39;s OOP?

Ans - The purpose of Python's object-oriented programming (OOP) is to provide a way
to structure and organize code by representing real-world objects as classes and 
creating instances (objects) of those classes. OOP in Python allows you to define
classes with attributes (variables) and methods (functions), encapsulating data
and behavior together. It promotes code reusability, modularity, and easier 
maintenance by enabling concepts like inheritance, polymorphism, and encapsulation.
"""

"""
Q2. Where does an inheritance search look for an attribute?
Ans- When searching for an attribute in inheritance, Python looks for the attribute
in the following order:

The instance object itself.
The class of the instance object.
The superclasses (parent classes) of the class in the order they are defined.
The superclasses of each superclass, following the same order.
"""


"""
Q3. How do you distinguish between a class object and an instance object?

Ans- A class object is the blueprint or template for creating instances of that class.
An instance object, on the other hand, is a specific object created from a class,
representing a unique instance of that class.

"""

"""
Q4. What makes the first argument in a class’s method function special?

Ans- The first argument in a class's method function, conventionally named self,
refers to the instance of the class that the method is being called on. It allows
the method to access and manipulate the instance's attributes and methods.

"""
"""
Q5. What is the purpose of the __init__ method?

Ans- The __init__ method is a special method in Python classes that is called automatically
when a new instance of the class is created. It is used to initialize the attributes of the
instance and perform any other setup actions that are required before the instance can be used.

"""
"""
Q6. What is the process for creating a class instance?

Ans- To create a class instance, you simply call the class as if it were a function, passing any required arguments. For example, if the class is named MyClass, you can create an instance by writing my_instance = MyClass().

"""

"""
Q7. What is the process for creating a class?

Ans- To create a class in Python, you use the class keyword followed by the name of the class.
Inside the class, you define attributes and methods that describe the behavior and characteristics of the class.

"""

"""
Q8. How would you define the superclasses of a class?

Ans- The superclasses of a class, also known as parent classes or base classes, are the classes
from which the current class inherits. In Python, you define the superclasses by including them
in the parentheses after the class name during class creation. For example, if a class SubClass
inherits from a class SuperClass, the definition would be class SubClass(SuperClass). If there
are multiple superclasses, they can be separated by commas.

"""
