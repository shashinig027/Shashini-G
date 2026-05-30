# ==============================================================================
# PROJECT TITLE: E-Commerce Automated Order Audit & Revenue Verification
# AUTHOR: Shashini
# 
# SCENARIO / QUESTION:
# An e-commerce system suffered a database hiccup, causing some order records 
# to save corrupt data (such as negative prices or zero/negative quantities). 
# Before this financial data can be synced to the primary tracking system, 
# it must be sanitized.
#
# PROGRAM REQUIREMENTS:
# 1. Process a list of order records (dictionaries containing price & quantity).
# 2. Loop through the data to scan each transaction for corruption.
# 3. Flag and count any records where 'price' or 'quantity' is less than or equal to 0.
# 4. For valid records, calculate the line-item revenue (price * quantity).
# 5. Output a final summary reporting Total Revenue and Total Flagged Anomalies.
# ==============================================================================

# Your existing orders list goes right below this line...
print('-------order audit-------')
totalrevenue= 0
corrupted_count=0
while True:
    orders = [
    {"order_id": 101, "item": "Laptop", "price": 45000, "quantity": 1},
    {"order_id": 102, "item": "Mouse", "price": -500, "quantity": 2},     
    {"order_id": 103, "item": "Keyboard", "price": 1200, "quantity": 0},  
    {"order_id": 104, "item": "Monitor", "price": 15000, "quantity": 1},
    {"order_id": 105, "item": "Headphones", "price": 2500, "quantity": 3}
]
    for order in orders:
        if order["price"] < 0 or order["quantity"] <= 0:
            print(f"Corrupted order found: {order}")
            corrupted_count += 1
        else:
            totalrevenue += order["price"] * order["quantity"]
    print(f"Total Revenue: {totalrevenue}")
    print(f"Total Corrupted Orders: {corrupted_count}")
    break
