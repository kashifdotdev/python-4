def determine_age_category(age):
    if 0 <= age <= 12:
        return "You are a child."
    elif 13 <= age <= 19:
        return "You are a teenager."
    elif 20 <= age <= 59:
        return "You are an adult."
    elif age >= 60:
        return "You are a senior citizen."
    else:
        return "Invalid age input."

# Example usage
age = int(input("Enter your age: "))
print(determine_age_category(age))
