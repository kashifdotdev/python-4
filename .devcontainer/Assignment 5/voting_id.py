def check_voting_eligibility(age, nationality):
    if age >= 18:
        if nationality.lower() == "pakistani":
            return "You are eligible to vote."
        else:
            return "Please obtain a valid ID to vote."
    else:
        return "You are not eligible to vote due to age."

# Example usage
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
print(check_voting_eligibility(age, nationality))
