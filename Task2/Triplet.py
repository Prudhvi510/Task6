def find_triplet_with_sum(arr, target_sum):
    arr.sort()  # Sort the input list in ascending order
    triplets = []
    
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target_sum:
                triplets.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    
    return triplets

# Example usage:
input_list = [10, 20, 30, 9]
target_value = 59
triplets = find_triplet_with_sum(input_list, target_value)

if triplets:
    print("Triplets with the sum of", target_value, "are:")
    for triplet in triplets:
        print(triplet)
else:
    print("No triplet found with the sum of", target_value)