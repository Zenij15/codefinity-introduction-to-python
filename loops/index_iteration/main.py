prices = [29.99, 45.50, 12.75, 38.20]

#Set discount range
discount = [0.10, 0.20, 0.15, 0.05]

#Loop through price list
for i in range(len(prices)):
   new_price = prices[i] * (1 - discount[i])
   prices[i] = new_price
   updated_price = prices[i]
   print(f"Updated price for item {i}: ${updated_price:.2f}")

