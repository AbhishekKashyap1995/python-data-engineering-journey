# Functions Practice Questions

# 🟢 LEVEL 1 — Basics 

# 1️⃣ Write a function say_hello() that prints:
# Hello Data Engineer

def say_hello():
    print("Hello Data Engineer")

#----------------------------------------

# 2️⃣ Write a function add_numbers(a, b) that returns the sum.

def add_numbers(a,b):
    return a + b

#----------------------------------------

# 3️⃣ Write a function is_even(num) that returns True if number is even, else False.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Alternate

def is_even(num):
    return num % 2 == 0


#----------------------------------------

# 4️⃣ Write a function count_items(items) that returns the number of elements in a list.

items = ["1","2","3","76","87"]

def count_items(items):
    count = 0
    for item in items:
        count += 1
    return f"No of Elements : {count}"   

print(count_items(items))

# Alternate

def count_items(items):
    return len(items)


#----------------------------------------

# 5️⃣ Write a function get_first_item(data) that returns the first element of a list.
data = ["Abhishek", "Mohit", "Vishal"]

def get_first_item(data):
    return data[0]

print(get_first_item(data))

#----------------------------------------

# 🟡 LEVEL 2 — Real DE-Style Utility Functions

# 6️⃣ Write a function clean_text(text) that:

# Removes extra spaces
# Converts text to lowercase

# Input:

text =  "  Data ENGINEERING  "

# Output:

# "data engineering"

def clean_text(text):
    return text.strip().lower()

print(clean_text(text))

#----------------------------------------

# 7️⃣ Write a function is_valid_score(score) that returns True if score is between 0 and 100.

def is_valid_score(score):
    if 0 <= score <= 100:
        return True
    else :
        return False
    
print(is_valid_score(50))    

#----------------------------------------

# 8️⃣ Write a function calculate_average(numbers) that returns the average of a list.
numbers = [1,2,3,4,5,6,7,8,9]

def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total = total + num
        count += 1
    return total/count

print(calculate_average(numbers))    

# Alternate
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

#----------------------------------------

# 9️⃣ Write a function filter_high_scores(scores) that returns only scores >= 50

# (use loop, not lambda)

scores = [100,200,30,20,345,10,50]

def filter_high_scores(scores):
    result = []
    for score in scores:
        if score >= 50:
            result.append(score)
    return result        
                 
print(filter_high_scores(scores))

for value in filter_high_scores(scores):
    print(value)
#----------------------------------------

# 🔟 Write a function get_max_score(scores) using built-in functions only.

scores2 = [100,200,30,20,345,10,50]

def get_max_score(scores):
    return max(scores)

print(get_max_score(scores2))
#----------------------------------------

# 🔵 LEVEL 3 — Lambda & Built-ins (IMPORTANT)

# 1️⃣1️⃣ Convert this into a lambda function:
# def square(x):
#     return x * x

square = lambda x : x * x

print(square(9))

#----------------------------------------

# 1️⃣2️⃣ Use map() + lambda to convert:
data2 = [10, 20, 30]

# into:x
# [20, 40, 60]

doubled_value = list(map(lambda x: x * 2, data2))

print(doubled_value)

# 🔥 One-Line Definition (MEMORIZE)

# map() transforms data by applying the same function to every element.

# Alternate
added_ten = list(map(lambda x: x + 10, data2))

#----------------------------------------

# 1️⃣3️⃣ Use filter() + lambda to keep numbers greater than 25.
numbers3 = [23,12,54,24,65,32,789,111,21]

greater_than_25_number = list(filter(lambda x : x>25 , numbers3))

print(greater_than_25_number)

#----------------------------------------


# 1️⃣4️⃣ Use sorted() to sort this list descending:
numbers4 = [50, 20, 80, 10]

print(sorted(numbers4, reverse=True)) # to reverse the sort descending

#----------------------------------------

# 1️⃣5️⃣ Use zip() to combine:
names = ["Virat", "Rohit"]
scores = [80, 65]

# into printed output:

# Virat 80
# Rohit 65

for name,score in zip(names,scores):
    print(name,score)

#----------------------------------------

# 🔴 LEVEL 4 — Recursion (Confidence Builder)

# 1️⃣6️⃣ Write a recursive function print_numbers(n) that prints:
# Output:
# 3
# 2
# 1

# when n = 3

def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n = n - 1)

print_numbers(3)    

#----------------------------------------

# 1️⃣7️⃣ Write a recursive function sum_to_n(n) that returns sum of numbers from 1 to n.

# def sum_to_n(n):  # wrong thinking recursion and loops are different in working mechanism
#     total = 0
#     count = 0
#     if count == n:
#         return total  
#     count += 1
#     total = total + n
#     sum_to_n(n - 1)

def sum_to_n(n):
    if n == 1:          # ✅ Base condition
        return 1
    return n + sum_to_n(n - 1)

print(sum_to_n(5))

# 🔑 Golden Template for Recursion (USE THIS ALWAYS)    
# def recursive_function(n):
#     if base_condition:
#         return base_value
#     return work + recursive_function(smaller_problem)


#----------------------------------------


# 1️⃣8️⃣ What happens if you remove the base condition in recursion?

# Explain in one sentence.

# Ans : If base condition is absent function get called infinitely and crashed the software.

#----------------------------------------

# 🟣 LEVEL 5 — DE Thinking (MOST IMPORTANT)

# 1️⃣9️⃣ Why is returning values from functions better than printing in Data Engineering?

# Because when we return values we can use the value in other scenerios as store as list, store as variables, pass inside other functions, do calculations and many other.

# Polished Answer

# Returning allows values to be reused, tested, passed to other functions, and used in pipelines.

#----------------------------------------

# 2️⃣0️⃣ Convert this bad code into a function:

# ❌ Bad:

# total = 0
# for x in [10, 20, 30]:
#     total += x


# ✅ Write a function:

def total_value(val):
    total = 0
    for value in val:
        total = total + value
    return total

print(total_value([10,20,30]))
print(total_value([10,20,300]))