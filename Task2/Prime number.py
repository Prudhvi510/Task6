# Given list
original_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Initialize an empty list to store prime numbers
prime_numbers = []

# Iterate through the original list and find prime numbers
for number in original_list:
    if is_prime(number):
        prime_numbers.append(number)

# Print the count of prime numbers and the list of prime numbers
print("Count of prime numbers:", len(prime_numbers))
print("Prime numbers:", prime_numbers)