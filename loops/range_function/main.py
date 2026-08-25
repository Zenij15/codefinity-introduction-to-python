# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Loop each day for daily_promotions
for day in range(5):
    weekday = weekdays[day]
    promotions = daily_promotions[day]
    print(f"{weekday}: Promotion on {promotions}")