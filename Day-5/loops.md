# Day 5 — Python Loops

Loops are used to **repeat a block of code** multiple times.
They help avoid writing the same code again and again.

---

## Why Loops are Needed?

Without loops:

- You would repeat code manually
- Code becomes long and hard to manage

With loops:

- Code becomes shorter
- Easy to read and maintain

---

## Types of Loops in Python

1. `for` loop
2. `while` loop

---

## 1. `for` Loop

The `for` loop is used to iterate over a sequence like:

- list
- tuple
- string
- range

### Syntax

```python
for item in collection:
    # code to execute

```

Example 1: Loop through a list

scores = [45, 67, 89, 23]

for score in scores:
print(score)

Output:
45
67
89
23

2. while Loop

The while loop runs as long as the condition is True.

while condition: # code to execute

Example 2: Print numbers using while loop

count = 1

while count <= 5:
print(count)
count += 1

Output:
1
2
3
4
5

⚠️ Always update the condition inside while loop to avoid infinite loops.

3. break Statement

break is used to exit the loop immediately.

Example 3: Using break

scores = [45, 67, 89, 23]

for score in scores:
if score == 89:
break
print(score)

Output:
45
67

4. continue Statement

continue is used to skip the current iteration and move to the next one.

Example 4: Using continue

scores = [45, 67, 89, 23]

for score in scores:
if score < 50:
continue
print(score)

Output:
67
89

⭐ Interview Tip (Very Useful)

If interviewer asks:

“What happens when a variable is reassigned in Python?”

Answer:

“The variable now refers to the new object, and the old reference is lost unless stored elsewhere.”

#######################################

🔁 Loops Over Every Data Structure (Beginner → DE mindset)

1️⃣ Looping over a List
scores = [45, 67, 89, 23]

for score in scores:
print(score)

🧠 Think:

“Take one item at a time from a list”

2️⃣ Looping over a Tuple (same as list)

Tuple = read-only list

coordinates = (10, 20, 30)

for value in coordinates:
print(value)

✔ Same syntax
✔ Just can’t modify values

3️⃣ Looping over a String

A string is a sequence of characters.

name = "Virat"

for char in name:
print(char)

Output:

V
i
r
a
t

🧠 Useful in:

Data cleaning

Text parsing

Validation

4️⃣ Looping over a Dictionary (VERY IMPORTANT)

Dictionary = key : value pairs.

a) Loop over keys (default)
player = {
"name": "Virat",
"age": 35,
"team": "India"
}

for key in player:
print(key)

Output:

name
age
team

b) Loop over values
for value in player.values():
print(value)

Output:

Virat
35
India

c) Loop over key + value (MOST USED)
for key, value in player.items():
print(key, ":", value)

🧠 Data Engineering gold:

Reading JSON

APIs

Config files

5️⃣ Looping over a Set

Set = unique values (no duplicates)

ids = {101, 102, 103, 101}

for id in ids:
print(id)

✔ Order not guaranteed
✔ No duplicates

6️⃣ Looping using range() (numbers)
for i in range(5):
print(i)

Output:

0
1
2
3
4

Custom ranges
for i in range(1, 11):
print(i)

for i in range(0, 11, 2):
print(i)

🧠 Used for:

Index-based loops

Controlled iterations

7️⃣ Looping with index + value (enumerate)

Very important pattern.

players = ["Virat", "Rohit", "Rahul"]

for index, player in enumerate(players):
print(index, player)

Output:

0 Virat
1 Rohit
2 Rahul

8️⃣ Looping over multiple lists together (zip)
names = ["Virat", "Rohit", "Rahul"]
scores = [80, 90, 70]

for name, score in zip(names, scores):
print(name, score)

🧠 Real use:

Merging datasets

CSV row processing

9️⃣ Nested Loops (loop inside loop)
teams = ["India", "Australia"]
players = ["A", "B", "C"]

for team in teams:
for player in players:
print(team, player)

🧠 Used in:

Table data

Matrix processing

Cross joins

🔟 Looping over List of Dictionaries (REAL DE SCENARIO)
matches = [
{"team": "India", "score": 250},
{"team": "Australia", "score": 220}
]

for match in matches:
print(match["team"], match["score"])

🔥 This is core Data Engineering pattern.
