# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self._make = make    # Encapsulated attribute
        self._model = model  # Encapsulated attribute
        self._year = year    # Encapsulated attribute

    def display_info(self):
        print(f"{self._year} {self._make} {self._model}")

    def start_engine(self):
        print(f"The engine of the {self._make} {self._model} is starting...")

# Derived class
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

    def start_engine(self):
        super().start_engine()
        print(f"The {self._make} {self._model} car engine is now running smoothly.")

# Another derived class
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"Has sidecar: {'Yes' if self.has_sidecar else 'No'}")

    def start_engine(self):
        super().start_engine()
        print(f"The {self._make} {self._model} motorcycle engine is now running smoothly.")

# Polymorphism example
def start_vehicle_engine(vehicle):
    vehicle.start_engine()

# Encapsulation example
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

# Class method and static method example
class MathOperations:
    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Using the classes
if __name__ == "__main__":
    # Create instances of Car and Motorcycle
    car = Car("Toyota", "Camry", 2021, 4)
    motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, False)

    # Display information and start engines
    car.display_info()
    motorcycle.display_info()

    start_vehicle_engine(car)
    start_vehicle_engine(motorcycle)

    # Using the BankAccount class
    account = BankAccount("John Doe", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Account balance: ${account.get_balance()}")

    # Using class and static methods
    sum_result = MathOperations.add(10, 20)
    product_result = MathOperations.multiply(10, 20)
    print(f"Sum: {sum_result}, Product: {product_result}")
