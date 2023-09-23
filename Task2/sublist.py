def has_sublist_with_zero_sum(input_list):
    prefix_sum = 0
    prefix_sums_set = set()

    for num in input_list:
        prefix_sum += num
        
        # If the current prefix sum is zero or has been encountered before, there's a sublist with a zero sum.
        if prefix_sum == 0 or prefix_sum in prefix_sums_set:
            return True
        
        prefix_sums_set.add(prefix_sum)

    # If no sublist with zero sum is found, return False.
    return False

# Example usage:
input_list = [4, 2, -3, 1, 6]
result = has_sublist_with_zero_sum(input_list)

if result:
    print("There is a sublist with a zero sum.")
else:
    print("There is no sublist with a zero sum.")