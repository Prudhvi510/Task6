# Given list
original_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is a happy number
def is_happy_number(number):
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    return number == 1

# Initialize a counter for happy numbers
happy_count = 0

# Iterate through the original list and count happy numbers
for number in original_list:
    if is_happy_number(number):
        happy_count += 1

# Print the count of happy numbers
print("Count of happy numbers:", happy_count)