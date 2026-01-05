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
