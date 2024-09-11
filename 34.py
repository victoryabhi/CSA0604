'''
34.To Implement a function median_of_medians(arr, k) that takes an unsorted array arr and an integer k, and returns the k-th smallest element in the array.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] k = 6
arr = [23, 17, 31, 44, 55, 21, 20, 18, 19, 27] k = 5
Output: An integer representing the k-th smallest element in the array.

Closest Pair of Points(Divide and Conquer)

'''
def median_of_medians(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    # Split arr into sublists of 5
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    
    # Find the median of medians
    pivot = median_of_medians(medians, len(medians) // 2) if len(medians) > 1 else medians[0]
    
    # Partitioning step
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)
    
    if k <= len(low):
        return median_of_medians(low, k)
    elif k > len(low) + pivot_count:
        return median_of_medians(high, k - len(low) - pivot_count)
    else:
        return pivot

# Example usage
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k1 = 6
print(median_of_medians(arr1, k1))  # Output: 6

arr2 = [23, 17, 31, 44, 55, 21, 20, 18, 19, 27]
k2 = 5
print(median_of_medians(arr2, k2))  # Output: 20
