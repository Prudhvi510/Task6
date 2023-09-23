# Given list
original_list = [10, 501, 22, 100, 999, 87, 351]

# Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the original list
for number in original_list:
    if number % 2 == 0:
        even_numbers.append(number)  # Add even numbers to the even_numbers list
    else:
        odd_numbers.append(number)  # Add odd numbers to the odd_numbers list

# Print the resulting lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)