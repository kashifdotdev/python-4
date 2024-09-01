def calculate_percentage():
    # Ask the user for the obtained marks and the total marks
    obtained_marks = float(input("Enter the obtained marks: "))
    total_marks = float(input("Enter the total marks: "))

    # Calculate the percentage
    percentage = (obtained_marks / total_marks) * 100

    # Print the result
    print(f"The percentage is {percentage:.2f}%.")

# Call the function
calculate_percentage()
