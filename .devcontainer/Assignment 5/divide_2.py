def check_divisibility(number):
    if number % 2 == 0 and number % 3 == 0:
        return f"{number} is divisible by both 2 and 3"
    elif number % 2 == 0:
        return f"{number} is divisible by 2"
    elif number % 3 == 0:
        return f"{number} is divisible by 3"
    else:
        return f"{number} is not divisible by 2 or 3"

# Example usage
number = int(input("Enter a number: "))
print(check_divisibility(number))
