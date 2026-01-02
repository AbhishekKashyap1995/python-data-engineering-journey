1️⃣ NoneType
What is None?

None represents the absence of a value.

result = None
print(result)
print(type(result))

When is None used?

Placeholder variables

Functions that return nothing

Initializing variables before assigning real data

Interview Tip:

None is not zero, not empty, and not False.
It represents “no value”.

2️⃣ list — Ordered, Mutable Collection

A list stores multiple values in a single variable.

numbers = [10, 20, 30]
names = ["Amit", "Ravi", "Neha"]

Key Properties:

Ordered

Mutable (can be changed)

Allows duplicate values

Accessing elements:
print(numbers[0]) # 10

Modifying a list:
numbers.append(40)
numbers[1] = 25

3️⃣ tuple — Ordered, Immutable Collection

A tuple is like a list, but cannot be changed.

coordinates = (10, 20)

Difference from list:
coordinates[0] = 15 # ❌ Error

When to use tuples?

Fixed data (coordinates, constants)

Data safety

4️⃣ dict — Key-Value Data Structure

Very important for real-world applications and data engineering.

product = {
"name": "Cricket Bat",
"price": 1200,
"in_stock": True
}

Access values:
print(product["price"])

Update values:
product["price"] = 1100

Why dictionaries matter:

Used in APIs

JSON data

Database records

5️⃣ set — Unordered, Unique Values

A set stores unique elements only.

numbers = {1, 2, 3, 3, 2}
print(numbers) # {1, 2, 3}

Use cases:

Remove duplicates

Membership checking

---

| Type    | Ordered | Mutable | Allows Duplicates |
| ------- | ------- | ------- | ----------------- |
| `int`   | ❌      | ❌      | ❌                |
| `float` | ❌      | ❌      | ❌                |
| `str`   | ✅      | ❌      | ✅                |
| `list`  | ✅      | ✅      | ✅                |
| `tuple` | ✅      | ❌      | ✅                |
| `dict`  | ✅      | ✅      | Keys ❌           |
| `set`   | ❌      | ✅      | ❌                |

Interview Questions:

1️⃣ Why does input() always return a string?

input() returns a string because Python cannot assume what type of data the user intends to enter.

When a user types something:

Python reads it as text from the keyboard

Text input is safest to store as a string

Converting it automatically could cause errors or data loss

Therefore, Python leaves the responsibility to the programmer to explicitly convert the input to int, float, or another type when needed.

Example:

age = input("Enter your age:") # always string
age = int(age) # explicit conversion

Interview line:

input() returns a string so that the programmer has full control over how and when the data is converted.

2️⃣ Difference between list and tuple
Feature List Tuple
Mutability Mutable (can be changed) Immutable (cannot be changed)
Syntax [] ()
Performance Slightly slower Slightly faster
Use case Dynamic data Fixed data
Example:

# List

scores = [80, 90, 85]
scores.append(95)

# Tuple

coordinates = (10, 20)

# coordinates[0] = 15 ❌ Error

When to use a list:

When data needs to change

User inputs

Collections you modify

When to use a tuple:

Constant values

Fixed records

Data safety

Interview line:

I use lists for mutable data and tuples for fixed, read-only data to prevent accidental modification.

3️⃣ When would you prefer float over int?

You prefer float when:

Decimal precision is required

Calculations involve fractions

Financial, scientific, or measurement data is involved

Example:
price = 99.99 # float
quantity = 2 # int
total = price \* quantity

Using int here would lose decimal precision, leading to incorrect results.

Interview line:

I prefer float over int when accuracy matters and decimal values must be preserved.

✅ Summary (One-Line Answers)

input() returns string → Because user input is textual and type conversion must be explicit.

List vs Tuple → List is mutable, tuple is immutable.

Float vs Int → Float is used when decimal precision is required.
