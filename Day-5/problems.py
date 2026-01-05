# 🟢 Level 1 — Basics (Warm-up)

# Q1. Print all scores

# Given:
scores = [45, 67, 89, 23, 90]
# 👉 Use a for loop to print each score on a new line.

for score in scores :
    print(score)

#----------------------------------------

# Q2. Print only even numbers

# Given:
numbers = [1, 4, 7, 10, 13, 16]
# 👉 Print only the even numbers.

for num in numbers:
    if num % 2 == 0:
        print(num)

#----------------------------------------

# Q3. Count items in a list

# Given:
players = ["Virat", "Rohit", "Rahul", "Pant", "Abhishek"]
# 👉 Count how many players are there without using len().

count = 0

for num in players:
    count += 1

print(count)

#----------------------------------------

# 🟡 Level 2 — Conditions + Loops

# Q4. Filter high match scores

# Given:
scores2 = [120, 95, 110, 45, 78]

# 👉 Print scores that are 100 or more.

for score in scores2:
    if score >= 100:
        print(score)

#----------------------------------------

# Q5. Sum of all scores

# Given:
scores3 = [40, 60, 80, 20]

# 👉 Calculate the total score using a loop.

total = 0

for score in scores3:
    total += score

print(total)

#----------------------------------------

# Q6. Skip low scores (continue)

# Given:
scores4 = [120, 30, 95, 20, 110]

# 👉 Skip scores below 50 and print the rest using continue.

for score in scores4:
    if score < 50:
        continue
    print(score)

#----------------------------------------

# 🔵 Level 3 — break, while, thinking

# Q7. Stop loop when score is found

# Given:
scores5 = [45, 67, 89, 23, 90]

# 👉 Stop the loop when score equals 89 using break.

for score in scores5:
    if score == 89:
        break
    print(score)

#----------------------------------------

# Q8. Print numbers using while

# 👉 Use a while loop to print numbers from 1 to 10.

num = 1

while num <= 10:
    print(num)
    num += 1

#----------------------------------------

# Q9. Find first high score

# Given:
scores6 = [30, 45, 60, 110, 95]

# 👉 Print the first score greater than 100 and stop the loop.

for score in scores6:
    if score > 100:
        print(score)
        break

#----------------------------------------

# 🔴 Level 4 — Real understanding check

# Q10. Count passes and fails

# Given:
scores7 = [35, 80, 45, 90, 60, 30]

# Rules:
# Pass: score ≥ 50
# Fail: score < 50

# 👉 Print:
# Pass count: X
# Fail count: Y

pass_count = 0
fail_count = 0

for score in scores7:
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1    

print(f"Pass Count : {pass_count}")
print(f"Fail Count : {fail_count}")