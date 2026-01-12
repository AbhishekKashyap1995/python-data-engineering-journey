import csv     # importing csv module

with open("cricket-match.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Try skip header and print total runs

total_runs = 0

with open("cricket-match.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # skips header

    for row in reader:
        runs = int(row[1])
        total_runs += runs

print("Total Runs:", total_runs, header)   

# Using DictReader (csv.DictReader) Best Way

total_balls = 0

with open("cricket-match.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_balls += int(row["balls"])

print("Total Balls:", total_balls)

# Finding Highest Run Scorer

highest_runs_scorer = ""
highest_runs = 0

with open("cricket-match.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["runs"]) > highest_runs:
            highest_runs = int(row["runs"])
            highest_runs_scorer = row["player"]

print("Top Scorer:", highest_runs_scorer, "-", highest_runs)


# Counting Number of Records
count = 0

with open("cricket-match.csv", "r") as file:
    reader = csv.DictReader(file)

    for _ in reader:
        count += 1

print("Total Players:", count)

# Writing Data to a CSV File

# data = [
#     ["player", "runs", "balls"],
#     ["Gill", 65, 42],
#     ["Surya", 38, 25]
# ]

# with open("new_match.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# Writing CSV using DictWriter

# data = [
#     {"player": "Gill", "runs": 65, "balls": 42},
#     {"player": "Surya", "runs": 38, "balls": 25}
# ]

# with open("match_summary.csv", "w", newline="") as file:
#     fieldnames = ["player", "runs", "balls"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerows(data)

