# Defining a class named Person
class Person:
    # Constructor method to initialize the object
    def __init__(self, name, age, city):
        self.name = name  # Instance variable for name
        self.age = age    # Instance variable for age
        self.city = city  # Instance variable for city


    # Method to display person details
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

# Creating an instance of the Person class
person1 = Person("John Doe", 30, "New York")

# Accessing the method to display information
person1.display_info()

# Creating another instance of the Person class
person2 = Person("Jane Smith", 25, "Los Angeles")

# Accessing the method to display information
person2.display_info()
