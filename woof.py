 #Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # A generic implementation
        raise NotImplementedError("Subclass must implement this abstract method")

# Child class inheriting from Animal
class Dog(Animal):
    # Overriding the parent's speak method
    def speak(self):
        return f"{self.name} says Woof!"

# Another child class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of the classes
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.speak()) # Output: Buddy says Woof!
print(my_cat.speak()) # Output: Whiskers says Meow!