Conditional Statements (if / elif / else)

Conditional statements allow a program to make decisions based on conditions.
They control the flow of execution in a Python program.

---

## What are Conditional Statements?

Conditional statements execute different blocks of code depending on whether
a condition is **True** or **False**.

**Real-world example:**

- If it rains → take an umbrella
- Else → go without umbrella

---

## Basic `if` Statement

The `if` statement runs a block of code only when the condition is True.

```python
runs = 75

if runs > 50:
    print("Half century!")

--------------------------------------------
if – else Statement
Used when there are exactly two possible outcomes.

python
Copy code
runs = 30

if runs >= 50:
    print("Good innings")
else:
    print("Needs improvement")

----------------------------------------------
if – elif – else Statement
Used to check multiple conditions.

python
Copy code
runs = 85

if runs >= 100:
    print("Century!")
elif runs >= 50:
    print("Half century!")
else:
    print("Low score")
Python evaluates conditions from top to bottom.
The first True condition gets executed.

------------------------------------------------

Comparision operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |


Think like a Data Engineer (important mindset)

A Data Engineer uses conditionals for:

Data quality checks
Threshold alerts
Categorization
Business rules
Pipeline branching

Example:

if records_count == 0:
    print("Pipeline failed: No data")


This is real DE work.

------------------------------------------

Data Engineer Rule of Thumb

Use else when:

-There is a default or fallback state
-You want a catch-all safety net
-Input might be unexpected or dirty

Skip else when:

-All logical states are explicitly handled
-Each failure reason must be precise
-You want clear failure diagnostics

#  Differnce between codes

Code 1: Direct print() inside conditions
if extract and transform and load:
    print("ETL Success")
elif not extract:
    print("Extraction Failed")
elif not transform:
    print("Transformation Failed")
elif not load:
    print("Load Failed")

🔍 What this code does

Checks conditions

Immediately prints output

Ends execution

✅ Pros

✔ Simple
✔ Easy to read
✔ Good for learning & small scripts

❌ Cons (Important)

Output is not reusable

You cannot:

Save the result

Send it to a file

Send it to a database

Return it from a function

Hard to test in real pipelines

🧠 DE Reality

In real Data Engineering:

We don’t just print

We log, store, alert, or return

This code is learning-level, not production-level.

🧩 Code 2: Assign result to a variable (DE-style)
if extract and transform and load:
    status = "ETL Success"
elif not extract:
    status = "Extraction Failed"
elif not transform:
    status = "Transformation Failed"
elif not load:
    status = "Load Failed"

print(status)

🔍 What this code does

Determines ETL status

Stores it in a variable

Uses it later

✅ Pros (Very Important)

✔ Reusable
✔ Testable
✔ Production-ready
✔ Clean separation of logic & output

You can now do:

log(status)
save_to_db(status)
send_alert(status)
return status

❌ Cons

Slightly more lines (but worth it)

🔥 Key Difference (THIS IS THE CORE)
Aspect	Code 1	Code 2
Purpose	Show output	Determine state
Reusability	❌ No	✅ Yes
Testing	❌ Hard	✅ Easy
Production	❌ No	✅ Yes
DE Standard	❌	✅
🧠 Data Engineer Analogy (Very Important)
Code 1 = Talking

“The pipeline succeeded.”

Code 2 = Recording

“The pipeline status is SUCCESS, now act on it.”

Data Engineering is about recording & acting, not just speaking.

🚀 Real-World Example
❌ Bad pipeline
print("Pipeline Failed")

✅ Good pipeline
status = "Pipeline Failed"
send_slack_alert(status)
write_log(status)

🧠 Final Rule (Remember this forever)

Never mix decision logic with output logic in production code

That’s why Code 2 is superior.

```
