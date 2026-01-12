📘 CSV Files in Python

1. What is a CSV File?

CSV (Comma-Separated Values) is a simple, text-based file format used to store tabular data.

Example:

player,runs,balls
Rohit,45,32
Virat,72,50
Rahul,28,20

Key Characteristics

Each line = one record (row)

Columns separated by commas

First row usually contains headers

Widely used in data pipelines, ETL jobs, analytics

2. Why CSV is Important in Data Engineering

CSV files are commonly used for:

Raw data ingestion

Data exchange between systems

Logs and reports

Source files in ETL pipelines

Almost every Data Engineer works with CSV files.

3. Python csv Module

Python provides a built-in csv module to work with CSV files safely and efficiently.

import csv

4. Reading a CSV File using csv.reader
   Basic Example
   import csv

with open("cricket_match.csv", "r") as file:
reader = csv.reader(file)
for row in reader:
print(row)

Output
['player', 'runs', 'balls']
['Rohit', '45', '32']
['Virat', '72', '50']
['Rahul', '28', '20']

⚠️ All values are read as strings

5. Skipping Header Row

In data processing, headers are often skipped.

import csv

with open("cricket_match.csv", "r") as file:
reader = csv.reader(file)
header = next(reader)

    for row in reader:
        print(row)

6. Calculating Total Runs (Real-World Example)
   import csv

total_runs = 0

with open("cricket_match.csv", "r") as file:
reader = csv.reader(file)
next(reader)

    for row in reader:
        total_runs += int(row[1])

print("Total Runs:", total_runs)

7. Using csv.DictReader (Recommended ✅)

DictReader reads each row as a dictionary using column names.

Example
import csv

with open("cricket_match.csv", "r") as file:
reader = csv.DictReader(file)

    for row in reader:
        print(row)

Output
{'player': 'Rohit', 'runs': '45', 'balls': '32'}

8. Total Runs using DictReader (Best Practice)
   import csv

total_runs = 0

with open("cricket_match.csv", "r") as file:
reader = csv.DictReader(file)

    for row in reader:
        total_runs += int(row["runs"])

print("Total Runs:", total_runs)

✔ Cleaner code
✔ No column index confusion
✔ Industry preferred

9. Finding Highest Run Scorer
   import csv

max_runs = 0
top_player = ""

with open("cricket_match.csv", "r") as file:
reader = csv.DictReader(file)

    for row in reader:
        runs = int(row["runs"])
        if runs > max_runs:
            max_runs = runs
            top_player = row["player"]

print("Top Scorer:", top_player, "-", max_runs)

10. Counting Number of Records
    import csv

count = 0

with open("cricket_match.csv", "r") as file:
reader = csv.DictReader(file)

    for _ in reader:
        count += 1

print("Total Players:", count)

11. Writing Data to a CSV File
    import csv

data = [
["player", "runs", "balls"],
["Gill", 65, 42],
["Surya", 38, 25]
]

with open("new_match.csv", "w", newline="") as file:
writer = csv.writer(file)
writer.writerows(data)

12. Writing CSV using DictWriter
    import csv

data = [
{"player": "Gill", "runs": 65, "balls": 42},
{"player": "Surya", "runs": 38, "balls": 25}
]

with open("match_summary.csv", "w", newline="") as file:
fieldnames = ["player", "runs", "balls"]
writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

13. Common CSV Mistakes

❌ Forgetting to convert strings to int
❌ Not skipping header
❌ Using column index instead of column name
❌ Not using newline="" while writing

14. Data Engineering Best Practices

✔ Always validate data types
✔ Use DictReader for clarity
✔ Handle missing values
✔ Log errors during ingestion
✔ Keep raw CSV files unchanged

15. Summary

CSV files are foundational in Data Engineering

Python csv module is lightweight and powerful

DictReader is the preferred approach

CSV is often the first step in ETL pipelines

######################

🧠 Data Engineering Rule (VERY IMPORTANT)
❗ Never name files as:

csv.py
json.py
time.py
sys.py
random.py
