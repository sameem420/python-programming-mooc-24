# Write your solution here
temperature = int(input("Please type in a temperature (F): "))
temperature_celsius = (temperature - 32) * (5/9)
print(f"{temperature} degrees Fahrenheit equals {temperature_celsius} degrees Celsius")
if temperature_celsius < 0:
    print("Brr! It's cold in here!")