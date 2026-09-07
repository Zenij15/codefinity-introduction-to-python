# Call the function and print the result
def calculate_total_cost(cost_of_item, sold_items):
    total_cost = cost_of_item * sold_items
    return total_cost    

apples_total_cost = calculate_total_cost(1.50, 10)

print(f"The total cost for apples is ${apples_total_cost}")