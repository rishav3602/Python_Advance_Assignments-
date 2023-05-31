"""
Q1. What is the difference between __getattr__ and __getattribute__?

Ans 1. The key difference between __getattr__ and __getattribute__ lies in their purpose and when they are invoked:

__getattr__ is a special method that gets called when an attribute lookup fails. It is only invoked
when the requested attribute is not found via the normal process of attribute lookup. It is a fallback
mechanism to dynamically provide attributes that are not explicitly defined on an object.

__getattribute__ is a special method that gets called for every attribute access, regardless of whether
the attribute exists or not. It is invoked before __getattr__ and allows you to intercept and customize
the attribute access behavior. However, it is important to be cautious when implementing __getattribute__
to avoid infinite recursion by calling the attribute lookup on self within the method.

Q2. What is the difference between properties and descriptors?

Ans 2. Properties and descriptors are both mechanisms for controlling attribute access in Python, 
but they differ in terms of their usage and implementation:

Properties: Properties are a way to add additional behavior to attribute access and modification
of an object. They are defined as methods within a class and are accessed like normal attributes,
but behind the scenes, they execute custom code when accessed, set, or deleted. Properties provide
a clean and convenient way to encapsulate attribute access logic without directly exposing the underlying
implementation.

Descriptors: Descriptors are a lower-level mechanism for defining attribute access and modification behavior.
They are defined as separate classes and can be shared among multiple attributes of different objects.
Descriptors use special methods like __get__, __set__, and __delete__ to define the behavior when an
attribute is accessed, set, or deleted. They offer more control and flexibility but require a deeper 
understanding of the descriptor protocol.

Q3. What are the key differences in functionality between __getattr__ and __getattribute__, as well as properties and descriptors?

Ans 3. The key differences in functionality between __getattr__, __getattribute__, properties, and descriptors are as follows:

__getattr__ and __getattribute__:
__getattr__ is invoked only when an attribute is not found via the normal attribute lookup process.
__getattribute__ is invoked for every attribute access, regardless of whether the attribute exists or not.
__getattr__ is a fallback mechanism to provide attributes dynamically.
__getattribute__ allows customization and interception of attribute access behavior, but must be used with caution to avoid infinite recursion.

Properties and descriptors:

Properties are defined as methods within a class and allow for customization of attribute access behavior
using the @property, @attribute.setter, and @attribute.deleter decorators.
Descriptors are separate classes that define the behavior of attribute access, modification, and deletion using the __get__, __set__, and __delete__ methods.
Properties provide a high-level, convenient interface for attribute access control and can be used within a single class.
Descriptors offer a lower-level, more flexible mechanism that can be shared among multiple attributes or classes.

"""
