def calculate_rectangle_area():
    # Ask the user for the length and width of the rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area
    area = length * width

    # Print the result
    print(f"The area of the rectangle is {area} square units.")

# Call the function
calculate_rectangle_area()
