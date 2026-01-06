🔥 Most Used Python Built-in Functions for Data Engineering

1️⃣ print() – Debugging & Logging (Beginner stage)
What it does

Displays output on screen.

print("Pipeline started")

DE use case

Check intermediate data

Debug transformations

⚠️ In production → replaced by logging

2️⃣ len() – Count Records (VERY COMMON)
Example
records = ["row1", "row2", "row3"]
print(len(records))

DE use case

Count rows in dataset

Validate data after filtering

if len(data) == 0:
print("No data received")

3️⃣ type() – Data Validation
Example
print(type(10))
print(type("abc"))

DE use case

Validate incoming data types

Debug schema issues

4️⃣ sum() – Aggregations
Example
scores = [10, 20, 30]
print(sum(scores))

DE use case

Total sales

Total runs

Metrics aggregation

5️⃣ min() / max() – Boundary Checks
Example
prices = [99, 250, 150]
print(min(prices))
print(max(prices))

DE use case

Lowest / highest value detection

Data quality checks

6️⃣ sorted() – Ordering Data
Example
scores = [45, 10, 80]
print(sorted(scores))

Descending:

print(sorted(scores, reverse=True))

DE use case

Top N records

Ranking data

7️⃣ enumerate() – Index + Value Together (IMPORTANT)
Example
players = ["Virat", "Rohit", "Dhoni"]

for index, player in enumerate(players):
print(index, player)

Output
0 Virat
1 Rohit
2 Dhoni

DE use case

Row numbering

Debug record positions

8️⃣ zip() – Combine Multiple Lists (VERY COMMON)
Example
names = ["Virat", "Rohit"]
scores = [80, 65]

for name, score in zip(names, scores):
print(name, score)

DE use case

Merge parallel datasets

Combine columns

9️⃣ map() – Transform Data (CORE)
Example
scores = [30, 40, 50]
new_scores = list(map(lambda x: x + 10, scores))

map() does NOT return a list in Python 3.
It returns a map object (iterator).
list() is used to convert it into a list so you can see/use the values.

Output:

[40, 50, 60]

DE use case

Apply transformation to every record

Data normalization

🔟 filter() – Remove Bad Data (CORE)
Example
scores = [30, 65, 80]
passed = list(filter(lambda x: x >= 50, scores))

filter() does NOT return a list in Python 3.
It returns a map object (iterator).
list() is used to convert it into a list so you can see/use the values.

DE use case

Filter invalid records

Data quality enforcement

1️⃣1️⃣ any() / all() – Data Validation
Example
scores = [60, 70, 80]

print(all(score >= 50 for score in scores))
print(any(score < 50 for score in scores))

output will be : True/False

DE use case

Validate dataset

Check rules across rows

1️⃣2️⃣ dict() – Build Structured Data
Example
keys = ["name", "score"]
values = ["Virat", 80]

record = dict(zip(keys, values))
print(record)

DE use case

Create structured rows

JSON-like data

############################

DE DAILY-USE SUMMARY (MEMORIZE)

| Function          | Why DEs Use It |
| ----------------- | -------------- |
| `len()`           | Count rows     |
| `sum()`           | Aggregation    |
| `min()` / `max()` | Range checks   |
| `sorted()`        | Ranking        |
| `zip()`           | Merge datasets |
| `map()`           | Transform      |
| `filter()`        | Clean data     |
| `enumerate()`     | Index rows     |
| `any()` / `all()` | Validation     |
