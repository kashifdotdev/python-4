# Ask the user for the number of seconds
total_seconds = int(input("Enter the number of seconds: "))

# Calculate the number of minutes and remaining seconds
minutes = total_seconds // 60
seconds = total_seconds % 60

# Print the result
print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")
