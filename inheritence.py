# What is inheritance in Python oops and types of Inheritance?
# Inheritance in Python is a way for one class (called the child class or subclass) to gain the properties and behaviors 
# (attributes and methods) of another class (called the parent class or superclass).

# class Parent:
#     # Parent class code

# class Child(Parent):
    # Child class code inherits from Parent
# Types of Inheritance in Python:
# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance
# ---------------------------------------------------------------------------------------------------------------------
# ) Single Inheritance:

# A child class inherits from one parent class.

# In the single inheritance, when we create an object of the chlid class then we are able to access the properties of the chlid class as well as its parent class.

# Example:

# class Animal:
#     def speak(self):
#         print("Animal sound")

# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         print("Woof!")

# dog = Dog()
# dog.speak()
# dog.bark()  