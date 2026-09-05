# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

combined_list = list(zip(products, prices, quantities_sold))   # combines the lists into tuples
sorted_products = sorted(combined_list)

for i in sorted_products:
    name = i[0]
    price = i[1]
    quantity = i[2]
    for name, price, quantity in sorted_products:
      print(f"Product: {name}\n, Price: {price}\n, Quantity Sold: {quantity}")  