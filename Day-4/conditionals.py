# Basic If statement:

if True: # Checks condition If true then code runs otherwise doesn't happen anything
    print("This is True")


# If-else statement:

score = 100

# Only one code block runs if condition satisfies than if block runs otherwise else block run

if score < 50 :
    print("Less Score")
else :
    print("High Score")    

# If-elif-else Statement:  

runs = 85

# Python evaluates conditions from top to bottom.
# The first True condition gets executed.  

if runs >= 100:
    print("Century!")
elif runs >= 50:
    print("Half century!")
else:
    print("Low score")


# Practice 1: Match Result Logic

# Problem:

# If score ≥ 300 → "Match Won"
# If score between 200–299 → "Competitive Match"
# Else → "Match Lost"

score = 500

if score >= 300:
    print("Match Won")
elif 299 >= score >=  200:
    print("competitive match")
else:
    print("Match Lost")     

# Practice 2: Grade Calculator

# Rules:

# 90–100 → A
# 75–89 → B
# 50–74 → C
# Below 50 → Fail    

score = 44

if score >= 90:
    print("A")
elif score >= 75:
    print("B") 
elif score >= 50:
    print("C")
else:
    print("Fail")  

