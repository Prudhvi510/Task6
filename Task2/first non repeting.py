def first_non_repeating_element(input_list):
    element_count = {}
    
    # Count the occurrences of each element in the list
    for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    # Find the first non-repeating element
    for element in input_list:
        if element_count[element] == 1:
            return element
    
    # Return None if no non-repeating element is found
    return None

# Example usage:
input_list = [2, 3, 5, 3, 7, 2, 5, 8]
result = first_non_repeating_element(input_list)

if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found in the list.")