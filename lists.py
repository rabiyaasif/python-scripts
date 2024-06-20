# Creating a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Printing the original list
print("Original list of fruits:", fruits)

# Accessing elements by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding a new element to the end of the list
fruits.append("fig")
print("List after adding a fruit:", fruits)

# Inserting an element at a specific position
fruits.insert(2, "grape")
print("List after inserting a fruit at index 2:", fruits)

# Removing an element by value
fruits.remove("banana")
print("List after removing 'banana':", fruits)

# Removing an element by index
removed_fruit = fruits.pop(3)  # Removes the element at index 3
print("List after popping the fruit at index 3:", fruits)
print("Removed fruit:", removed_fruit)

# Sorting the list
fruits.sort()
print("List after sorting:", fruits)

# Reversing the list
fruits.reverse()
print("List after reversing:", fruits)

# Slicing the list
print("Slicing the first three fruits:", fruits[:3])
print("Slicing from the second fruit to the end:", fruits[1:])

# List comprehension to create a new list with all fruits in uppercase
fruits_uppercase = [fruit.upper() for fruit in fruits]
print("List of fruits in uppercase:", fruits_uppercase)

# Checking if an item exists in the list
if "apple" in fruits:
    print("Apple is in the list of fruits.")

# Finding the length of the list
print("Number of fruits in the list:", len(fruits))

# Clearing the list
fruits.clear()
print("List after clearing all items:", fruits)
