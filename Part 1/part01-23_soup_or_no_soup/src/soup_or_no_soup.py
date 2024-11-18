# Write your solution here
name = input("Please tell me your name: ")
soup_portion_price = 5.90

if name == "Jerry":
    print("Next please!")
if name != "Jerry":
    soup_portions = int(input("How many portions of soup? "))
    print(f"The total cost is {soup_portions * soup_portion_price}")     
    print("Next please!")   