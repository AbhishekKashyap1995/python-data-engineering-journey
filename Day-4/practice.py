# 10 Conditional Practice Problems (DE-Focused)

# 🟢 Level 1 – Basics

# 1️⃣ Even or Odd

# Check if a number is even or odd.

num = 10

if num % 2 == 0 :
    print("Even")
else :
    print("Odd")    

# ---------------------------------------------

# 2️⃣ Age Category

# Age < 18 → Minor
# 18–60 → Adult
# 60 → Senior

age = 30

if age < 18 :
    print("Minor")
elif 60 >= age >= 18 :
    print("Adult")
else:
    print("Senior")         

# ❌ Slightly unclear for teams

# Improved version

if age < 18:
    print("Minor")
elif age <= 60:
    print("Adult")
else:
    print("Senior")


# ---------------------------------------------

# 3️⃣ Login Status

# If username is "admin" → Access Granted
# Else → Access Denied

username = "admin"

if username == "admin" :
    print("Access Granted")
else :
    print("Access Denied")    

# Improved version
# But DE systems often normalize input
# Prevents "Admin", "ADMIN" issues

if username.lower() == "admin":
    print("Access Granted")
else:
    print("Access Denied")

# ---------------------------------------------

# 🟡 Level 2 – Business Logic


# 4️⃣ Product Stock Check

# Stock = 0 → "Out of Stock"
# Stock < 10 → "Low Stock"
# Else → "In Stock"

stock = 10

if stock == 0 :
    print("Out of Stock")
elif stock < 10 :
    print("Low Stock")
else:
    print("In Stock")        

# ---------------------------------------------

# 5️⃣ Discount Eligibility

# Price ≥ 5000 → 20% discount
# Price ≥ 2000 → 10% discount
# Else → No discount

price = 7000

if price >= 5000 :
    print(f" {price}  Discount : {price * 0.2}")
elif price >= 2000 :
     print(f" {price}  Discount : {price * 0.1}")
else:
    print("No Discount")        

# ---------------------------------------------

# 6️⃣ Temperature Alert System

# Temp ≥ 45 → "Extreme Heat Alert"
# Temp ≥ 35 → "Heat Warning"
# Else → "Normal"

temp = 50

if temp >= 45:
    print("Extreme Heat Alert")
elif temp >= 35:
    print("Heat Warning")
else :
    print("Normal")        

# ---------------------------------------------

# 🔵 Level 3 – Data Engineering Style


# 7️⃣ Data Volume Check

# Records = 0 → "No Data – Stop Pipeline"
# Records < 1000 → "Small Batch"
# Else → "Large Batch"

records = 2000

if records == 0:
    print("No Data – Stop Pipeline")
elif records < 1000 :
    print("Small Batch")
else :
    print("Large Batch")        

# ---------------------------------------------

# 8️⃣ File Processing Status

# File exists → "Processing Started"
# File missing → "Pipeline Failed"

# (Hint: use a boolean variable)

file_exists = True

if file_exists:
    print("Processing Started")
else:
    print("Pipeline Failed") 

# ---------------------------------------------

# 9️⃣ Data Quality Check

# Null values > 10 → "Reject Dataset"
# Null values > 0 → "Clean Required"
# Else → "Dataset Valid"

null_values = 12

if null_values > 10:
    print("Reject Dataset")
elif null_values > 0 :
    print("Clean Required")
else :
    print("Dataset Valid")        

# ---------------------------------------------

# 🔴 Level 4 – Real-World Thinking

# 🔟 ETL Job Status

# Inputs:

extract = True
transform = True
load = False

# Rules:

# If all True → "ETL Success"
# If extract fails → "Extraction Failed"
# If transform fails → "Transformation Failed"
# If load fails → "Load Failed"

# if extract and transform and load == True:   Wrong way
#     print("ELT Success")
# elif extract == False:
#     print("Extract Failed")
# elif transform == False:
#     print("Transform Fail")
# elif load == False:
#     print("Load Fails")   

# Improved answer

if extract and transform and load:
    print("ETL Success")
elif not extract:
    print("Extraction Failed")
elif not transform:
    print("Transformation Failed")
elif not load:
    print("Load Failed")
  
# Even Better DE-Style (Optional Enhancement)

if extract and transform and load:
    status = "ETL Success"
elif not extract:
    status = "Extraction Failed"
elif not transform:
    status = "Transformation Failed"
elif not load:
    status = "Load Failed"

print(status)
