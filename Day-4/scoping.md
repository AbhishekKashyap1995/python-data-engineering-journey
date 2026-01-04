Variable Scope in Python (Beginner → DE Level)
What is Variable Scope?

Scope defines where a variable can be accessed (used) in your code.

In simple words:

Where a variable is created

Decides where it can be used

🟢 1️⃣ Global Scope
Example
status = "ETL Started"

def run_pipeline():
print(status)

run_pipeline()

Explanation

status is created outside the function

It is global

Can be accessed anywhere

✅ Works fine

🧠 DE use-case:

Configs

Constants

Environment flags

🔵 2️⃣ Local Scope (Most Important)
Example
def run_pipeline():
result = "Success"
print(result)

run_pipeline()
print(result) # ❌ ERROR

Why error?

result exists only inside the function

Outside → Python does not know it

🧠 DE use-case:

Intermediate results

Temporary data

Step outputs

🔴 3️⃣ Block Scope (Important Python Concept)

In Python:
❌ if / elif / else / loops do NOT create scope

Example
if True:
x = 10

print(x) # ✅ Works

This surprises many beginners.

🧠 DE note:

Variables inside conditionals are still accessible

⚠️ 4️⃣ Local vs Global Conflict
Example
status = "Not Started"

def run_pipeline():
status = "Running"
print(status)

run_pipeline()
print(status)

Output
Running
Not Started

Why?

Function created new local variable

Global variable remains unchanged

🧠 DE lesson:

Local variables shadow global ones

❗ 5️⃣ Using global keyword (Avoid in DE)
Example
status = "Not Started"

def run_pipeline():
global status
status = "Running"

run_pipeline()
print(status)

Works ❌ but BAD PRACTICE

🧠 Why avoid?

Hard to debug

Side effects

Breaks pipeline predictability

✔ Prefer return values

✅ 6️⃣ Correct DE Way: Return Values
def run_pipeline():
return "ETL Success"

status = run_pipeline()
print(status)

✔ Clean
✔ Testable
✔ Production-safe

🟣 7️⃣ Scope inside Loops
for i in range(3):
value = i \* 10

print(value) # ✅ Works

Loop does NOT create scope

value is accessible

🧠 DE note:

Be careful not to override important variables

🔥 8️⃣ Common Beginner Mistakes
❌ Using variable before defining
print(x) # NameError

❌ Expecting if-block to hide variable
if True:
secret = 123

print(secret) # Still accessible

📊 Scope Summary Table

| Scope Type      | Created Where     | Accessible Where  |
| --------------- | ----------------- | ----------------- |
| Global          | Outside functions | Everywhere        |
| Local           | Inside function   | Only inside       |
| Block (if/loop) | Python            | ❌ No block scope |
| Returned Value  | Function          | Caller            |

🧠 DE Golden Rules (Very Important)

1️⃣ Never rely on globals for pipeline state
2️⃣ Use functions + return values
3️⃣ Keep variables as local as possible
4️⃣ Pass data explicitly

🚀 Real DE Example

❌ Bad
data = []

def extract():
global data
data = load_data()

✅ Good
def extract():
return load_data()

data = extract()
