produce = ["Tomatoes", "Lettuce"]
dairy   = ["Milk", "Cheese"]

# Combine into a list of two sections
groceries = [produce, dairy]

for section in groceries:
    for item in section:
        print("Item Name:", item)