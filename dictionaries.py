# Creating a dictionary to store information about a person

person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "email": "john.doe@example.com"
}

# Accessing values in the dictionary
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Email:", person["email"])

# Adding a new key-value pair to the dictionary
person["phone"] = "555-1234"

# Modifying an existing key-value pair
person["email"] = "john.newemail@example.com"

# Removing a key-value pair from the dictionary
del person["age"]

# Iterating through the dictionary
print("\nUpdated person information:")
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists in the dictionary
if "name" in person:
    print("\nName exists in the dictionary.")

# Getting the value for a key with a default if the key does not exist
phone = person.get("phone", "Not Available")
print("Phone:", phone)
