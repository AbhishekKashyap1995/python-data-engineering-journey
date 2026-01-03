# PRACTICE — Cricket Players & Stats

players = {
    "Virat": 120,
    "Rohit": 95,
    "Gill": 80,
    "Rahul": 60
}

for name, score in players.items():
    print(name, "scored", score, "runs")

top_player = ""
top_score = 0

for name, score in players.items():
    if score > top_score:
        top_score = score
        top_player = name

print("Top Scorer:", top_player, "-", top_score)


# 2nd exercise

products = {
    "Bat": 4500,
    "Ball": 250,
    "Gloves": 1200
}

# Print: Bat costs 4500

# Print only expensive products (>1000)

print(products["Bat"])

for product in products:
    if products[product] > 1000 :
        print(product, "costs", products[product])

# Alternate method / best solution

for product, price in products.items():
    if price > 1000:
        print(product, "costs", price)

# 3rd Exercise

products = {
    "Bat": 4500,
    "Ball": 250,
    "Gloves": 1200
}
# 1️⃣ Print only product names
# 2️⃣ Print only prices
# 3️⃣ Print products between 500 and 5000

for product_name, product_price in products.items():
    print(product_name)

for product_name, product_price in products.items():
    print(product_price)

for product_name, product_price in products.items():    
    if product_price > 500 and product_price < 5000 :
        print(product_name, "price:", product_price)


# ⭐ PROFESSIONAL IMPROVEMENTS (Optional, but good habit)
# 🔹 Improvement 1: Use chained comparison (Pythonic)

for product_name, product_price in products.items():
    if 500 < product_price < 5000:
        print(product_name, "price:", product_price)

# ✔ Same result
# ✔ Cleaner
# ✔ Interview-friendly

# 🔹 Improvement 2: Use f-strings (industry style)

for product_name, product_price in products.items():
    if 500 < product_price < 5000:
        print(f"{product_name} price: {product_price}")

# Exercise 4

products = [
    {"name": "Bat", "price": 4500},
    {"name": "Ball", "price": 250},
    {"name": "Gloves", "price": 1200}
]

# Tasks:
# 1️⃣ Print all product names
# 2️⃣ Print products > 1000
# 3️⃣ Find the most expensive product

for product in products:
    print(product["name"])

for product in products:
    if product["price"] > 1000:
        print(product) 

expensive_price = 0
expensive_product = ""

for product in products:
    if product["price"] > expensive_price:
        expensive_price = product["price"]
        expensive_product = product["name"]

print(f"Most expensive product : {expensive_product} --> price : {expensive_price}")        