# MASTER REVISION (50 QUESTIONS)

# 🟢 SECTION 1: Python Basics & Types (Q1–Q8)

# 1️⃣ What is the output?

x = "10"
y = 5
# print(x * y)

# 👉 Python does NOT auto-convert strings to numbers.

# But actual output is 1010101010 don't know why 

# Correct Explanation (LOCK THIS 🔒)

# "10" is a string

#  with string means repetition, not math

# "10" * 5 → repeat "10" five times

# String repetition, not arithmetic


#--------------------------------------

# 2️⃣ Convert "100" to integer, add 50, and return the result using a function.

def convert_to_integer(value):
    return int(value) + 50

print(convert_to_integer("100"))
#--------------------------------------

# 3️⃣ Write a function that takes a value and returns its type.

def return_datatype(val):
    return type(val)

print(return_datatype("Abhishek"))
#--------------------------------------

# 4️⃣ What is the difference between:

# print(type(10))

# Displays output on screen, Cannot be reused

# and

# return type(10)

# Sends value back to caller, Can be stored, reused, tested

# ✅ Correct DE explanation

# print() is for display/debugging.
# return is for data flow and reuse in pipelines.

#--------------------------------------

# 5️⃣ Write a function that checks if a value is a string.

# def check_string_value(val):
#     if type(val) == type("String"):
#         return "Type String : True"        # Wrong Printing Strings instead of booleans
#     else:
#         return "Type String: False" 

# Alternate Solution

def check_string_value(val):
    return isinstance(val, str)

print(check_string_value(8))   
#--------------------------------------

# 6️⃣ Predict output:

# a = True
# b = False
# print(a + b)

# Output will be 1

#--------------------------------------


# 7️⃣ Write a function that converts a boolean into a string "Yes" or "No".

# def boolean_into_string(val):
#     if val == True:
#         return "Yes"
#     elif val == False:             # Wrong Answer
#         return "No"
#     else:
#         return "Not a boolean datatype"


#Alternate Solution

def boolean_into_string(val):
    if isinstance(val, bool):
        return "Yes" if val else "No"
    else:
        raise ValueError("Input must be boolean")
    
print(boolean_into_string(False))    

# 🔥 CRITICAL RULE (MEMORIZE THIS 🔒)

# In Python, the latest function definition with the same name wins.
# Earlier definitions are overwritten, not kept.

#--------------------------------------

# 8️⃣ Why is dynamic typing useful in Python for Data Engineering?

# Ans : Dynamic typing allows Python to handle different data types without explicit declarations, making it easier to process varied and evolving data sources in data pipelines.

#--------------------------------------

# 🟡 SECTION 2: Conditionals & Loops (Q9–Q18)

# 9️⃣ Write a function that checks if a number is positive, negative, or zero.

# def number_checker(num):
#     if num == 0:
#         return "Zero"
#     elif num > 0:
#         return "Positive Number"      # Ok Answer but failed on different Datatypes
#     elif num < 0:
#         return "Negative Number"
#     else:
#         return "Not a Number"          

# print(number_checker(10))

# 🧠 IMPORTANT RULE (MEMORIZE 🔒)

# Python does not auto-convert strings to numbers in comparisons.

# ✅ VERSION 1 — STRICT VALIDATION (Fail Fast)
def number_checker(num):
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a number")

    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive Number"
    else:
        return "Negative Number"

# VERSION 2 — FLEXIBLE CONVERSION (User-Friendly)
def number_checker(num):
    try:
        num = float(num)
    except ValueError:
        return "Not a Number"

    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive Number"
    else:
        return "Negative Number"

#--------------------------------------

# 🔟 What is the output?

for i in range(3):
    print(i)

# Output 0, 1, 2

#--------------------------------------


# 1️⃣1️⃣ Write a loop that prints only even numbers from 1 to 10.

num = 2
while num <= 10:
    print(num)
    num += 2

# Alternate for version

for num in range(2, 11, 2):
    print(num)

#--------------------------------------

# 1️⃣2️⃣ Write a function that returns the count of numbers greater than 50 in a list.
num = [20,45,67100,345,22,78,89,46,847,332]

def num_count_greater_than_50(val):
    count = 0
    for value in val:
        if value > 50:
            count += 1
    return count

print(num_count_greater_than_50(num))

# 🔥 KEY CONCEPT: VARIABLE SCOPE (MEMORIZE 🔒)
# Variable declared	Scope
# Inside function	Local
# Outside function	Global

# But ⚠️:

# You cannot modify a global variable inside a function unless you explicitly say so
#--------------------------------------

# 1️⃣3️⃣ What happens if you forget to update the loop variable in a while loop?

# Ans : Infinite Loop, because same input always and condition will always true.

#--------------------------------------

# 1️⃣4️⃣ Predict output:

# x = 5
# if x > 3:
#     if x < 10:
#         print("A")
#     else:
#         print("B")

# Output will be A.

#--------------------------------------


# 1️⃣5️⃣ Write a loop that stops when it finds the number 7.

i = 0
while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1

#--------------------------------------

# 1️⃣6️⃣ Difference between break and continue (1 sentence).

# Ans : Break will exit the loop immediately.
#       Continue will skip the element which meets condition

# ⭐ Polished DE version
# break stops the loop completely,
# while continue skips the current iteration and moves to the next one.

#--------------------------------------

# 1️⃣7️⃣ Write a function that sums all numbers in a list using a loop.

numbers_list = [1,2,3,4,5,6,7,8,9]

def sum_all_numbers(val):
    total = 0
    for number in val:
        total += number
    return total

print(sum_all_numbers(numbers_list))
#--------------------------------------

# 1️⃣8️⃣ Why are loops heavily used in data pipelines?

# Ans : ✅ Strong DE Answer (Use This)

# Loops are used in data pipelines to iterate over large datasets, process records step by step, apply transformations, and perform validations efficiently.

#--------------------------------------

# 🔵 SECTION 3: Functions & Return vs Print (Q19–Q30)

# 1️⃣9️⃣ Write a function that prints "Hello" and returns "Done".

def print_hello_returns_done():
    print("hello")
    return "Done"

#--------------------------------------

# 2️⃣0️⃣ What is wrong with this function?

# def test():
#     print("Hello")
#     return
#     print("World")

# Solution : After return function immediately exit and print("World") never runs.

#--------------------------------------


# 2️⃣1️⃣ Write a function that takes a list and returns a new list with values doubled.

data1 = [1,2,3,4,5]

def doubled_values(val):
    doubled_data = []
    for data in val:
        doubled_data.append(data*2)
    return doubled_data

print(doubled_values(data1))

# Alternative

def doubled_values(val):
    return list(map(lambda x: x * 2, val))

#--------------------------------------

# 2️⃣2️⃣ Why should functions return values instead of printing them in DE?

# Ans : When return the value will return to caller can be used mutiple times in various types of operation. but printing only show output to console screen only good for debugging.

# ⭐ Polished DE-grade answer

# Returning values allows functions to be reused, tested, chained, and used in pipelines, while print is only for display/debugging.

#--------------------------------------

# 2️⃣3️⃣ What will this return?

# def f():
#     return print("Hi")

# print(f())

#   Ans : Hi
#       : None

# print() always returns None.
#--------------------------------------


# 2️⃣4️⃣ Write a reusable function that finds the maximum number in a list.

def find_max_number(val):
    return max(val)

print(find_max_number([100,20,30]))
print(find_max_number([100,20,30,400]))
#--------------------------------------

# 2️⃣5️⃣ Write a function that returns True if a list is empty.

data2 = []

def empty_list_status(val):
    if len(val) == 0:
        return True
    else:
        return False

print(empty_list_status(data2))
#--------------------------------------

# 2️⃣6️⃣ What happens if a function has no return statement?

# # Ans :  Correct Answer (IMPORTANT)

# If a function has no return statement, it returns None by default.

#--------------------------------------

# 2️⃣7️⃣ Convert this logic into a function:

# total = 0
# for x in [1, 2, 3]:
#     total += x

def total_sum(val):
    total = 0
    for x in val:
        total += x
    return total

print(total_sum([1,2,3,4,5,6]))
#--------------------------------------


# 2️⃣8️⃣ Write a function that cleans text (strip + lowercase).

def cleans_text(val):
    return val.strip().lower()
    
print(cleans_text("        Oh-No"))
#--------------------------------------

# 2️⃣9️⃣ Why should function names be descriptive in production code?

# It is necesarry to have descriptive function names cause that helps to know the context what function does by just reading function name.

# ⭐ Stronger DE version

# Descriptive function names improve readability, maintainability, onboarding speed, and reduce bugs in large production codebases.

#--------------------------------------

# 3️⃣0️⃣ Can a function return multiple values? If yes, how?

# Ans : Yes, using tuple packing.

# 🔑 Golden Rule (MEMORIZE 🔒)

# Python functions return ONE object.
# If you see multiple values, they are packed into a tuple.
# Unpacking just splits them back into variables.

# Simplest Example (Even Smaller)
# def demo():
#     return 10, 20

# Calling:
# x = demo()
# print(x)


# Output:
# (10, 20)


# Unpacking:
# a, b = demo()

# Same as:

# a = 10
# b = 20
#--------------------------------------

# 🟣 SECTION 4: Built-in Functions, map, filter, zip (Q31–Q45)

# 3️⃣1️⃣ What does len() return?

# Ans : len() function return length of the elements.

# Ans better version : len() returns the number of items in an iterable.

#--------------------------------------

# 3️⃣2️⃣ Write a function that uses sum() and len() to calculate average.

def average(val):
    a = sum(val)
    b = len(val)
    return a/b 

print(average([1,2,3,4,5,6]))
#--------------------------------------

# 3️⃣3️⃣ Use map() to add 5 to every number in a list.

numbers3 = [1,2,300,4,5,50,101,546]

def addFive(val):
    return list(map(lambda val : val + 5 , val))

print(addFive(numbers3))
#--------------------------------------

# 3️⃣4️⃣ Use filter() to keep numbers greater than 100.

def greaterThan100(val):
    return list(filter(lambda val : val > 100, val))

print(greaterThan100(numbers3))
#--------------------------------------

# 3️⃣5️⃣ Why does map() need list() in Python?

# Ans : map() returns a map object (iterator).
#       list() is used to convert it into a usable list.

#     map_obj = map(int, ["1", "2"])
#     list(map_obj)  # [1, 2]


#--------------------------------------

# 3️⃣6️⃣ What is the difference between map() and for loop?

# Ans : map() applies a function to all elements in one line.
        
        # 💡 Interview-Friendly Line

        # map() applies the same function( A function is just some operation. ) to every element of an iterable and returns the transformed result.


      # for loop is more flexible and allows complex logic.

# map
list(map(lambda x: x*2, [1,2,3]))

# for loop
result = []
for x in [1,2,3]:
    result.append(x*2)

#--------------------------------------

# 3️⃣7️⃣ What does this output?

# list(zip([1,2], [10,20], [100,200]))

# Output
# [(1,10,100),(2,20,200)]

#--------------------------------------

# 3️⃣8️⃣ What happens if lists passed to zip() have different lengths?

# Output : zip only zips when the lists length is same. If one is shorter or vice versa zip immediately stop the operation.

list(zip([1,2,3], [10,20]))
# [(1,10), (2,20)]


#--------------------------------------

# 3️⃣9️⃣ Write a loop using zip() that prints name and score.

names = ["Abhishek", "Mohit", "Vicky", "Ajay"]
scores = [100, 50, 150, 200]


for i in list(zip(names, scores)):
    print(i)

# Better Alternative Version
for name, score in zip(names, scores):
    print(name, score)

#--------------------------------------

# 4️⃣0️⃣ Convert this using map():

# def square(x):
#     return x * x

# map() needs an iterable

# 99 is an integer, not iterable

def square(x):
    return list(map(lambda x : x*x, x))

print(square([99,23]))

# 🧠 Interview One-Liner

# Iterable = An object that can return its elements one at a time.

# ❌ What is NOT Iterable?
# x = 100
# for i in x:   # ❌ ERROR
#     print(i)


# ❌ Integers
# ❌ Floats
# ❌ None

#--------------------------------------


# 4️⃣1️⃣ Use sorted() to sort a list descending.

list4 = [34,12,15,-678,42,124]

def sortedValuesDescending(values):
    return sorted(values, reverse=True)

print(sortedValuesDescending(list4))
#--------------------------------------

# 4️⃣2️⃣ Difference between min() and max().

# Ans max() gives the largest element from an iterable.
    # min() gives the smallest element from an iterable.

#--------------------------------------

# 4️⃣3️⃣ Use any() to check if any value is negative in a list.

def checksNegativeValue(val):
    return any(x < 0 for x in val)

print(checksNegativeValue(list4))

#--------------------------------------

# 4️⃣4️⃣ Use all() to check if all values are positive.

list5 = [1,2,3,45,6,7,85,45,22,35]

def checksAllPositiveValues(val):
    return all(x > 0 for x in val)

print(checksAllPositiveValues(list5))

#--------------------------------------

# 4️⃣5️⃣ Why are built-in functions faster than custom loops?

# Ans : Built-in functions are faster because they are implemented in optimized C code
    #   and avoid Python-level loop overhead.

#     📌 Interview-friendly line:

#      Built-in functions are optimized and run at a lower level than Python loops.


#--------------------------------------

# 🔴 SECTION 5: Recursion (Light & Conceptual) (Q46–Q50)

# 4️⃣6️⃣ What are the two mandatory parts of a recursive function?

# Ans:
# 1. Base condition (stopping condition)
# 2. Recursive call (function calling itself)

#--------------------------------------

# 4️⃣7️⃣ Why is recursion risky without a base condition?

# Ans : It will cause infinite looping.

# Better Answer

# It causes infinite recursion and leads to stack overflow.

#--------------------------------------

# 4️⃣8️⃣ Convert this recursive logic into a loop (conceptually):

# sum_to_n(n)

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_to_n(5))  # 15

#--------------------------------------

# 4️⃣9️⃣ In one sentence:
# Is recursion important for Data Engineering? Why / Why not?

# Ans : Recursion is generally not important in Data Engineering because iterative and
#       distributed processing is more efficient and scalable.

# Simplified Answer

# No, recursion is not very important in Data Engineering because loops and big-data tools handle large data better.


#--------------------------------------

# 5️⃣0️⃣ When would you avoid recursion in real-world data processing?

# Ans : Recursion should be avoided when processing large datasets because it can
#       cause stack overflow and is inefficient compared to loops or distributed systems.

#Simplified Answer

# We avoid recursion when working with large data because it can crash the program and loops are safer.

# 🧠 Ultra-Short Memory Trick

# Recursion → small problems

# Loops / Big-data tools → large data
