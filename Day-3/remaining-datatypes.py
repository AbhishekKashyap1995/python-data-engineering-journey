# List

players = ["Abhishek", "Mohit", "Vishal"]

print(players)
print(players[0])   # access items
print(players[1])   # access items

players.append("Ajay")  # modifying lists
print(players)
players[3] = "Ajay Dipri" # modifying lists

print(players)


# Tuples -> read only lists

match_info = ("IND", "AUS", 2025)
print(match_info)
match_info[0] = "ENG"  # TypeError: 'tuple' object does not support item assignment


# Sets

teams = {"India", "Australia", "India", "England"}
print(teams)

teams.add("South Africa")
print(teams)

# ✅ WHEN SHOULD YOU USE SETS?

# ✔ When you need:

# Unique values
# Fast lookup
# No concern about order


# Dictionaries

player = {
    "name": "Virat Kohli",
    "runs": 12000,
    "team": "India"
}

# Access values

print(player["name"])
print(player["runs"])

# Update and Add

player["runs"] = 12500  # update
player["centuries"] = 75 # Add

print(player)
