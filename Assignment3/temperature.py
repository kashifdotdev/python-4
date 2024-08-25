# Ask the user for the temperature and the conversion type
temperature = float(input("Enter the temperature: "))
conversion_type = input("Convert to (C)elsius or (F)ahrenheit? Enter C or F: ").strip().upper()

# Convert the temperature
if conversion_type == "C":
    # Fahrenheit to Celsius
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {celsius:.2f}°C")
elif conversion_type == "F":
    # Celsius to Fahrenheit
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {fahrenheit:.2f}°F")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
