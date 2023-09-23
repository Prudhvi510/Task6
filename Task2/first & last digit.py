# Function to find the sum of the first and last digits of an integer
def sum_of_first_and_last_digit(number):
    # Convert the number to a string to work with individual digits
    number_str = str(number)
    
    # Extract the first and last digits
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    
    # Calculate the sum of the first and last digits
    sum_result = first_digit + last_digit
    
    return sum_result

# Example usage:
integer_value = 123456
result = sum_of_first_and_last_digit(integer_value)
print("Sum of first and last digits:", result)