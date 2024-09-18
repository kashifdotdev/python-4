def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Taking input from the user
num = int(input("Enter a positive integer to calculate its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")
