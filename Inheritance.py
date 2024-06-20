# Defining a base class named Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This is a placeholder method to be overridden by subclasses

# Defining a subclass named Dog that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the constructor of the base class
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

# Defining a subclass named Cat that inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Calling the constructor of the base class
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"


# Creating instances of Dog and Cat
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")

# Accessing methods
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

# Accessing attributes
print(f"{dog.name} is a {dog.breed}")  # Output: Buddy is a Golden Retriever
print(f"{cat.name} is a {cat.color} cat")  # Output: Whiskers is a Tabby cat
