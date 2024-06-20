# Function without parameters and without return value
def greet():
    print("Hello, World!")

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Function with a return value
def add(a, b):
    return a + b

# Function with default arguments
def describe_person(name, age=25, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Using the functions
if __name__ == "__main__":
    # Calling a function without parameters
    greet()

    # Calling a function with parameters
    greet_person("Alice")

    # Calling a function with a return value
    result = add(3, 5)
    print(f"Sum: {result}")

    # Calling a function with default arguments
    describe_person("Bob")
    describe_person("Charlie", 30)
    describe_person("Dave", city="New York")
