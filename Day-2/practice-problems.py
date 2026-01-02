# Practice Problems (Day 2 Focused)

#  Practice 1 — Variable & Type Check

value = "100"

# Tasks:

# Print its data type
# Convert it to integer
# Add 50 and print the result

# Solution
print(type(value))
value = int(value)
print(value + 50)
print(type(value))

# ------------------------------------

#  Practice 2 — Boolean Logic

price = 1200
discount = 200

# Task: Create a variable is_discounted that stores True if final price is less than 1000.

# Solution

final_price = price - discount
is_discounted = final_price

if final_price < 1000 :
    print(True)
else :
    print(False)  

# Below is better version of solution

final_price = price - discount
is_discounted = final_price < 1000

print(is_discounted)

# Boolean expressions in Python directly return True or False, so no if-else is required here.

# ------------------------------------

# Practice 3 — List Operations

scores = [80, 75, 90, 85]

# Tasks:

# Add a new score 88
# Replace 75 with 78
# Print the final list

# Solution

scores.append(88)
scores[1] = 78
print(scores)

# ------------------------------------

# Practice 4 — Dictionary Basics

student = {
    "name": "Abhishek",
    "marks": 85
}

# Tasks:

# Add a new key passed (True if marks ≥ 40)
# Update marks to 90
# Print the dictionary

# Solution

student["passed"] = student["marks"] >= 40

student["marks"] = 90

print(student)

# ------------------------------------

# Practice 5 — Calculator Upgrade

# Modify your calculator to:
# Accept decimal numbers
# Print output using f-strings
# Print the result rounded to 2 decimal places

# Hint:round(value, 2)

num1 = input("Please enter 1st number")
num2 = input("Please enter 2nd number")

num1 = float(num1)
num2 = float(num2)

print(f"Addition : {round(num1 + num2, 2)}")
print(f"Subtraction : {round(num1 - num2, 2)}")
print(f"Division : {round(num1 / num2, 2)}")
print(f"Multiplication : {num1 * num2:.2f}")