start_number = 5
countdown_values = []

# Create variable current number, setting it to start number
current_number = start_number

# Set while loop to count down
while current_number > 0:
    countdown_values.append(current_number)
    current_number = current_number - 1
print("Discount countdown complete!")
print(countdown_values)
        