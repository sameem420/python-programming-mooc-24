# Write your solution here
eat_times_weekly = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
weekly_grocery_price = float(input("How much money do you spend on groceries in a week? "))
weekly_cafe_spend = eat_times_weekly * lunch_price
print("Average food expenditure:")
print(f"Daily: {(weekly_cafe_spend + weekly_grocery_price) / 7} euros")
print(f"Weekly: {weekly_cafe_spend + weekly_grocery_price} euros")