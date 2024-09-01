import math

def calculate_circle_area():
    # Ask the user for the radius of the circle
    radius = float(input("Enter the radius of the circle: "))

    # Calculate the area
    area = math.pi * (radius ** 2)

    # Print the result
    print(f"The area of the circle is {area:.2f} square units.")

# Call the function
calculate_circle_area()
