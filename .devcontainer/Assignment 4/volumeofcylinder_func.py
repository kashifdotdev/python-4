import math

def calculate_cylinder_volume():
    # Ask the user for the radius and height of the cylinder
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))

    # Calculate the volume
    volume = math.pi * (radius ** 2) * height

    # Print the result
    print(f"The volume of the cylinder is {volume:.2f} cubic units.")

# Call the function
calculate_cylinder_volume()
