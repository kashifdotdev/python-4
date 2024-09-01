def calculate_bmi():
    # Ask the user for their weight in kilograms and height in meters
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate the BMI
    bmi = weight / (height ** 2)

    # Print the result
    print(f"Your BMI is {bmi:.2f}.")

# Call the function
calculate_bmi()
