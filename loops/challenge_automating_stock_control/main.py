# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item in inventory:
    # 2. Unpack per-item values inside the loop
    current_stock, min_stock, restock_amount, on_sale = inventory[item]
    
    # 3. Restock until we hit the minimum
    while current_stock < min_stock:
        current_stock += restock_amount

    # 4. Save updated stock
    inventory[item][0] = current_stock

    # 5. Mark on sale if above threshold
    if current_stock > discount_threshold and not on_sale:
        inventory[item][3] = True

print("Processing completed")