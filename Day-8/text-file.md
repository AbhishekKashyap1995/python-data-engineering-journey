## 📖 Reading a Text File

### Basic way

```python
file = open("log.txt", "r")
content = file.read()
print(content)
file.close()
"r" → read mode

read() → reads full file as a string

✅ Best Practice: Using with

with open("log.txt", "r") as file:
    content = file.read()
    print(content)
Automatically closes the file

Safer and cleaner

🖨 Output (looks like this):
Server started
User logged in
Error occurred
Process finished


📌 Internally:

content = "Server started\nUser logged in\nError occurred\nProcess finished\n"

#################

📄 Reading File Line by Line

with open("log.txt", "r") as file:
    for line in file:
        print(line.strip())
Useful for log files

.strip() removes extra spaces and newlines

🖨 Output (looks the SAME):
Server started
User logged in
Error occurred
Process finished


But internally it does this:

line = "Server started\n"
line = "User logged in\n"
line = "Error occurred\n"
line = "Process finished\n"

#####################

🔢 Counting Number of Lines

with open("log.txt", "r") as file:
    lines = file.readlines()
    print("Total lines:", len(lines))

🔹 file.readlines()

Reads all lines from file
Returns a list
Each line is a string ending with \n

📌 Internally:

lines = [
    "Server started\n",
    "User logged in\n",
    "Error occurred\n",
    "Process finished\n"
]

⚠️ Note (Interview Tip)

❌ readlines() is NOT good for huge files
✅ Better for small files only

########################

🔠 Counting Number of Words

word_count = 0

with open("log.txt", "r") as file:
    for line in file:
        words = line.split()
        word_count += len(words)

print("Total words:", word_count)

🔹 for line in file:

Reads file one line at a time

Memory-efficient ✅

📌 Internally:

line = "Server started\n"
line = "User logged in\n"
line = "Error occurred\n"
line = "Process finished\n"

🔹 line.split()

Splits line into words

Default separator = spaces

📌 Example:

"Server started\n".split()
# ['Server', 'started']

🧠 One-Line Memory Trick

Lines → len(readlines())
Words → split() + len() + loop

####################

✍️ Writing to a Text File

with open("output.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("Day 8 Practice\n")

File Modes
"r" → read
"w" → write (overwrite)
"a" → append

🧠 Important Notes

Files must be closed after use

Always prefer with open()

Text files are common in data pipelines
```

###########################

🟢 Writing to a Text File in Python

1️⃣ Basic Writing ("w" mode)
Code
with open("output.txt", "w") as file:
file.write("Hello World\n")
file.write("Learning Python File Writing\n")

🔍 What happens?

"w" → write mode

Creates file if it does not exist
Deletes old content if file already exists
Writes text into the file

📄 File Content (output.txt)
Hello World
Learning Python File Writing

---

2️⃣ Important Rule: \n (New Line)
file.write("Line 1")
file.write("Line 2")

📄 Output:

Line 1Line 2

👉 Always add \n manually:

file.write("Line 1\n")
file.write("Line 2\n")

---

3️⃣ Append Mode ("a") — MOST USED
Code
with open("output.txt", "a") as file:
file.write("New log entry\n")

🔍 What happens?

"a" → append mode
Adds text at the end
Old data is safe

📌 Used in:

Logs
Daily reports
Data pipelines

---

4️⃣ Writing Multiple Lines (writelines())

lines = [
"Server started\n",
"User logged in\n",
"Process completed\n"
]

with open("log.txt", "w") as file:
file.writelines(lines)

⚠️ writelines() does NOT add \n automatically.

---

5️⃣ Writing Data from a Loop (Real-World Style)
logs = ["INFO Server up", "ERROR Disk full", "INFO Process done"]

with open("app.log", "w") as file:
for log in logs:
file.write(log + "\n")

---

6️⃣ Writing Numbers (Very Common Mistake)

❌ Wrong:
file.write(100)

✅ Correct:
file.write(str(100))

📌 Files accept strings only

---

7️⃣ Write + Read Together (Verification)

with open("data.txt", "w") as file:
file.write("Python\n")
file.write("Day 8\n")

with open("data.txt", "r") as file:
print(file.read())
