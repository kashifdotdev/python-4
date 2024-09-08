def check_number_status(number):
    if number > 0:
        return f"{number} is Positive"
    elif number < 0:
        return f"{number} is Negative"
    else:
        return f"{number} is Zero"

# Example usage
number = int(input("Enter a number: "))
print(check_number_status(number))
