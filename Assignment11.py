"""
Q1. What is the concept of a metaclass?

Ans 1. In Python, a metaclass is a class that defines the behavior and structure of other classes.
It is responsible for creating and initializing classes. Metaclasses allow you to control the creation
and behavior of classes at a higher level than regular class definitions. By defining a metaclass,
you can customize how classes are instantiated, how attributes are added or modified, and how methods
are defined and inherited.

Q2. What is the best way to declare a class's metaclass?

Ans 2. The best way to declare a class's metaclass in Python is by setting the __metaclass__ attribute
at the top of the class definition. Here's an example:



Q3. How do class decorators overlap with metaclasses for handling classes?

Ans 3. Class decorators and metaclasses both provide mechanisms for modifying the behavior of classes.
They overlap in the sense that they can both be used to add, modify, or remove attributes and methods
of a class. However, there are some differences between them:

Class decorators are functions or callable objects that take a class as input and return a modified version
of that class. They are applied directly to the class definition using the @decorator syntax. Class decorators
are executed immediately after the class definition is evaluated.

Metaclasses, on the other hand, are used to define the behavior and structure of classes at a higher level.
They operate at the time of class creation and are responsible for initializing and constructing classes.
Metaclasses are specified by setting the metaclass argument in the class definition or by using the __metaclass__ attribute.

While class decorators and metaclasses can achieve similar results, the main difference is in the level
at which they operate. Class decorators focus on modifying individual classes, while metaclasses provide
a higher-level control over the creation and behavior of classes.

Q4. How do class decorators overlap with metaclasses for handling instances?

Ans 4. Class decorators and metaclasses overlap in terms of modifying instances of classes indirectly.
While both can be used to customize the behavior of instances, the approaches differ:

Class decorators modify instances by adding, modifying, or wrapping methods and attributes of the class.
These modifications affect all instances of the class, as the class definition itself is modified.

Metaclasses can also indirectly modify instances by controlling the creation and initialization process 
of the class. By customizing the __new__() and __init__() methods of the metaclass, you can customize how
instances of the class are created and initialized. However, metaclasses have a broader scope and can also 
influence class-level behavior.

"""
