from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an animal.
    
    Abstraction:
    Abstraction is a fundamental principle of object-oriented programming (OOP) that involves hiding the
    implementation details of a class and only exposing the necessary features or behaviors to the outside world.
    It allows us to focus on what an object does rather than how it does it. In this Animal class, we define
    an abstract method make_sound() that must be implemented by subclasses. This ensures that all subclasses
    provide their own implementation of making a sound without revealing the internal details of how each
    animal makes its sound.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        """
        This is an Abstract method to make the animal sound.
        
        Notes:
        - This method must be overridden by subclasses to provide specific implementations.
        """
        pass

class Dog(Animal):
    """
    Class representing a dog, inheriting from Animal.
    """
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    """
    Class representing a cat, inheriting from Animal.
    """
    def make_sound(self):
        return "Meow!"

class Duck(Animal):
    """
    Class representing a duck, inheriting from Animal.
    """
    def make_sound(self):
        return "Quack!"
