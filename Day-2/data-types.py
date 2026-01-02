# Data Types
# Python automatically detects the type of data stored in a variable.

# | Data Type | Example         | Description     |
# | --------- | --------------- | --------------- |
# | `int`     | `10`            | Whole numbers   |
# | `float`   | `10.5`          | Decimal numbers |
# | `str`     | `"Hello"`       | Text data       |
# | `bool`    | `True`, `False` | Logical values  |

quantity = 3 # integer datatype

price = 101.5 # float datatype

product_name = "Cricket Bat" # String datatype

in_stock = True # Boolean Datatype
is_active = False # Boolean Datatype


# How to check Datatype

print(type(quantity))
print(type(in_stock))


# Type Casting

# Why is type casting needed?

# User input from input() is always received as a string, even if the user enters a number.

age = input("Enter Your Age: ")
print(type(age))  # <class 'str'>

# To perform calculations, we must convert it.

# Converting Between Types

age = int(age)
price = float("99.5")
count = str(10)
