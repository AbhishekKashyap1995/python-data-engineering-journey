# Day 6 — Python Functions

## What is a Function?

A function is a reusable block of code that performs a specific task.

Functions help:

- Avoid repeating code
- Make programs clean and readable
- Organize logic like real-world Data Engineering pipelines

Think of a function as:
Input → Process → Output

---

## Why Functions are Important for Data Engineers

In Data Engineering, almost everything is written as functions:

- Extract data
- Transform data
- Load data

Each step is usually one function.

Example:

```python
extract_data()
transform_data()
load_data()
```

Basic Function Syntax

def function_name(): # code block

Example:

def greet():
print("Hello Data Engineer")

greet()

#####################

Functions with Parameters (Inputs)

Parameters allow functions to accept data.

def greet(name):
print("Hello", name)

greet("Abhishek")

name → parameter

"Abhishek" → argument

##############################

Functions with Return Values

return sends data back from the function.

def add(a, b):
return a + b

result = add(10, 20)
print(result)

######################

Print vs Return

print() → only displays output

return → gives output to the program (preferred in DE)

####################################

Practice: Batting Average Function

Formula:
batting_average = total_runs / matches

def batting_average(total_runs, matches):
return total_runs / matches

Usage:

avg = batting_average(450, 10)
print(avg)

##########################

Reusable Utility Functions

Utility functions perform small, reusable tasks.

Example: Clean Player Name
def clean_name(name):
return name.strip().title()

Usage:

print(clean_name(" virat kohli "))

#############################

Example: Boolean Utility Function

def is_high_score(score):
return score >= 50

Usage:

scores = [30, 65, 80, 45]

for score in scores:
if is_high_score(score):
print(score, "is a high score")

###########################

🔹 Types of Functions in Python

Broadly, Python functions can be divided into 6 main types.

1️⃣ Built-in Functions (Already provided by Python)

These functions are ready-made. You don’t need to define them.

Examples:
print()
len()
type()
sum()
max()
min()

Example:
scores = [30, 65, 80]
print(len(scores)) # 3
print(max(scores)) # 80

📌 Data Engineer usage
Used daily for quick operations on data.

2️⃣ User-Defined Functions (Most Important)

Functions you create yourself using def.

Example:
def batting_average(runs, matches):
return runs / matches

Usage:

avg = batting_average(450, 10)

📌 DE Insight
Most ETL pipelines are written using user-defined functions.

3️⃣ Functions With / Without Parameters
🔹 Without parameters
def greet():
print("Hello")

🔹 With parameters
def greet(name):
print("Hello", name)

📌 Parameters make functions dynamic.

4️⃣ Functions With / Without Return Value
🔹 Without return (only prints)
def show_message():
print("Process completed")

🔹 With return (recommended)
def get_total(a, b):
return a + b

📌 Rule for DE
Prefer return → easier to reuse and test.

5️⃣ Lambda Functions (One-Line Functions)

Small, anonymous functions.

Example:
square = lambda x: x \* x
print(square(5)) # 25

📌 Used with:

map()

filter()

sorted()

DE example:
scores = [30, 65, 80]
high_scores = list(filter(lambda x: x >= 50, scores))

6️⃣ Recursive Functions (Function calling itself)

Used rarely, but good to know.

Example:
def countdown(n):
if n == 0:
return
print(n)
countdown(n - 1)

📌 Rare in DE, but useful in algorithms.

🔥 DE-STYLE PRACTICAL CLASSIFICATION (VERY IMPORTANT)
In real Data Engineering, functions are written as:
1️⃣ Utility Functions

Small helper functions

def clean_name(name):
return name.strip().title()

2️⃣ Transformation Functions

Modify data

def apply_discount(price):
return price \* 0.9

3️⃣ Validation Functions

Return True/False

def is_valid_score(score):
return score >= 0

4️⃣ Pipeline Functions

Big functions calling other functions

def run_pipeline():
extract()
transform()
load()

🧠 One-Line Summary (MEMORIZE THIS)

Python has built-in and user-defined functions.
User-defined functions can have parameters, return values, can be lambda or recursive.
Data Engineers mostly use clean, reusable user-defined functions.

##################

🔹 PART 1: Lambda Functions (ONE-LINE FUNCTIONS)
🧠 First: Why Lambda Exists?

Normally, you write functions like this 👇

def square(x):
return x \* x

Python says:

“If function bahut chhota hai (one line), shortcut use karo”

That shortcut = lambda

🔹 Lambda Syntax (Don’t Memorize Yet)

lambda arguments: expression

⚠️ Rule:

Only ONE line

Automatically returns value

No def, no function name

🔹 Example 1: Square Number
Normal function
def square(x):
return x \* x

Same using lambda
square = lambda x: x \* x

Use it:

print(square(5))

Output:

25

🧠 Read it like English:

“square equals lambda that takes x and returns x \* x”

🔹 Example 2: Add Two Numbers
add = lambda a, b: a + b
print(add(3, 4))

🔹 Where Lambda is ACTUALLY Used (Important)

Lambda is mostly used inside other functions.

🔹 Lambda with filter() (DE Real Example)
scores = [30, 65, 80, 45]

high_scores = list(filter(lambda x: x >= 50, scores))

print(high_scores)

Step-by-step:

filter() → checks each item

lambda x: x >= 50 → rule

If True → keep

If False → remove

Output:

[65, 80]

Equivalent normal function:

def is_high_score(x):
return x >= 50

🔥 When to Use Lambda (RULE)

✅ Use lambda when:

Logic is small

Used only once

Readable in one line

❌ Avoid lambda when:

Logic is complex

Multiple steps

Need debugging

###############################

🔹 PART 2: Recursive Functions (Function Calling Itself)
🧠 First: Simple Meaning

A recursive function is a function that calls itself.

def countdown(n):
if n == 0: # 1️⃣ STOP condition
return
print(n) # 2️⃣ Do work
countdown(n - 1) # 3️⃣ Call itself again

🔹 Should Data Engineers Use Recursion?
Short Answer: Rarely ❌

DEs prefer:

for loops

vectorized operations

simple readable code

Recursion is mostly for:

Algorithms

Tree structures

Interviews

🔥 Lambda vs Normal vs Recursion (Quick Table)

| Type            | Use Case              |
| --------------- | --------------------- |
| Normal Function | Most DE logic         |
| Lambda          | Small, one-time logic |
| Recursive       | Rare, special cases   |
