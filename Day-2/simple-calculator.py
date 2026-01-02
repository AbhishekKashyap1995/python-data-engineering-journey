# Practice Project — Simple Calculator
# Goal:

# Create a program that:

# Accepts two numbers from the user

# Performs basic arithmetic operations

num1 = input("Please enter 1st number")
num2 = input("Please enter 2nd number")

num1 = float(num1)
num2 = float(num2)

print("Addition :", num1 + num2)
print("Subtraction :", num1 - num2)
print("Division :", num1 / num2)
print("Multiplication :", num1 * num2)


# Interview Answer
# “I use float() when I want to preserve decimal precision in calculations.
# int() is used only when I am certain the value will always be a whole number. 
# For calculators or financial data, float() is generally preferred to avoid data loss.”

# using int in conversion : Decimals are truncated, not rounded.
# float Handles both integers and decimals
# Safer for calculators
# Used in real-world applications (billing, analytics, finance)

# String Formatting (Professional Output)
# Recommended Method: f-strings

total = 500
print(f"The total amount is ₹{total}")


name = "Abhishek"
score = 92

print(f"{name} scored {score} marks.")
