"""
1.What is the concept of an abstract superclass?
Ans- An abstract superclass, also known as an abstract base class (ABC), is a class that is designed to be inherited from but not instantiated directly. It provides a common interface and defines abstract methods that its subclasses must implement. An abstract superclass serves as a blueprint for its subclasses and provides a way to enforce certain behavior or structure in the subclasses.

2.What happens when a class statement's top level contains a basic assignment statement?
Ans- When a class statement's top level contains a basic assignment statement, it creates a class attribute. This attribute is shared by all instances of the class and can be accessed using the class name or any instance of the class.

3.Why does a class need to manually call a superclass's init method?
Ans- When a class inherits from a superclass, it needs to explicitly call the superclass's __init__ method to ensure that the superclass's initialization code is executed. By calling the superclass's __init__ method, the subclass can initialize any inherited attributes and perform any necessary setup actions defined in the superclass.

4.How can you augment, instead of completely replacing, an inherited method?
Ans- To augment an inherited method instead of completely replacing it, you can use method overriding. Method overriding allows a subclass to provide its own implementation of a method that is already defined in its superclass. By defining a method with the same name in the subclass, the subclass can add functionality to the existing method by calling the superclass's method using the super() function and then performing additional actions.

5.How is the local scope of a class different from that of a function?
Ans- The local scope of a class refers to the namespace inside the class block. It includes class attributes, methods, and any local variables defined within methods. The class's local scope is accessible by all methods of the class.

On the other hand, the local scope of a function refers to the namespace inside the function block. It includes function parameters, any local variables defined within the function, and any variables defined within nested blocks. The local scope of a function is limited to that specific function and is not accessible outside of it.

"""