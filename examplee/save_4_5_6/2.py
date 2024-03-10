import re

def is_phone_number(input_string):
    # Define the pattern for a phone number
    pattern = r'^\+?(\d{1,3})?\s?[-.\(\)]?\d{3}[-.\(\)]?\s?\d{3}[-.\(\)]?\s?\d{4}$'
    
    # Check if the input string matches the pattern
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Test the function
phone_number = input("Enter a phone number: ")
if is_phone_number(phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")