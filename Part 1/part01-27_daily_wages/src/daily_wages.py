# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day_of_week = input("Day of the week: ")

if day_of_week == "Sunday":
    print(f"Daily wages: {(hourly_wage * 2) * hours_worked} euros")
if day_of_week != "Sunday":    
    print(f"Daily wages: {hourly_wage * hours_worked} euros")