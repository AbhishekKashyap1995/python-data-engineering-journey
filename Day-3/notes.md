# 📘 Day 3 — Python Data Types (Core Data Structures)

These data types are the foundation of Python and are heavily used in
Data Engineering, APIs, databases, and data pipelines.

---

## 1️⃣ Lists

### What is a List?

- Ordered collection
- Mutable (can be changed)
- Allows duplicate values

### Example

```python
players = ["Virat", "Rohit", "Gill"]
print(players)
Access elements
python
Copy code
print(players[0])    # Virat
print(players[-1])   # Gill
Modify list
python
Copy code
players.append("Rahul")
players[1] = "Rohit Sharma"
Key Points
Order is maintained

Index-based access

Most commonly used data type

Use Case
CSV rows

API responses

User input data

------------------------------------------------------------

2️⃣ Tuples
What is a Tuple?
Ordered collection

Immutable (cannot be changed)

Faster and safer than lists

Example
python
Copy code
match_info = ("India", "Australia", 2025)
print(match_info)
❌ This will cause error:

python
Copy code
# match_info[0] = "England"
Key Points
Fixed data

Cannot add/remove elements

Used for constant values

Use Case
Configuration values

Database rows

Coordinates, settings

----------------------------------------------------------------

3️⃣ Sets
What is a Set?
Unordered collection

Stores only unique values

No indexing

Very fast lookup

Example
python
Copy code
teams = {"India", "Australia", "India", "England"}
print(teams)
➡ Duplicate values are automatically removed.

Add elements
python
Copy code
teams.add("South Africa")
Important Behavior ⚠️
Order is NOT guaranteed

Output order may change every run

This is expected and correct behavior

Why order changes?
Sets use hashing internally

Hashing focuses on speed, not order

Convert set to ordered form
python
Copy code
sorted_teams = sorted(teams)
print(sorted_teams)
Use Case
Removing duplicates

Unique user IDs

Unique country or category names

------------------------------------------------------------------------

4️⃣ Dictionaries (MOST IMPORTANT 🔥)
What is a Dictionary?
Key → Value pairs

Unordered (but stable in modern Python)

Extremely important in real-world data

Example
python
Copy code
player = {
    "name": "Virat Kohli",
    "team": "India",
    "runs": 120
}
Access values
python
Copy code
print(player["name"])
print(player["runs"])
Update / Add values
python
Copy code
player["runs"] = 125
player["centuries"] = 75
Iterate dictionary
python
Copy code
for key, value in player.items():
    print(key, ":", value)
Use Case
JSON data

API responses

Database records

Configuration files
```

| Data Type | Ordered          | Mutable | Duplicates  | Use Case        |
| --------- | ---------------- | ------- | ----------- | --------------- |
| List      | ✅ Yes           | ✅ Yes  | ✅ Yes      | General data    |
| Tuple     | ✅ Yes           | ❌ No   | ✅ Yes      | Fixed data      |
| Set       | ❌ No            | ✅ Yes  | ❌ No       | Unique values   |
| Dict      | ⚠️ Logical order | ✅ Yes  | Keys unique | Structured data |

Lists maintain order, tuples are immutable,
sets store unique values without order,
dictionaries store structured key-value data.

🧠 RULES TO REMEMBER (WRITE THESE IN NOTES)

for x in dict → loops over keys

dict.items() → gives key + value

Use .items() when filtering by value

Strings don’t have .value
