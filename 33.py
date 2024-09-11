'''
33.To Implement the Median of Medians algorithm ensures that you handle the worst-case time complexity efficiently while finding the k-th smallest element in an unsorted array.
arr = [12, 3, 5, 7, 19] k = 2			Expected Output:5
arr = [12, 3, 5, 7, 4, 19, 26] k = 3		Expected Output:5
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] k = 6	Expected Output:6


'''

def median_of_medians(arr, k):
    if len(arr) < 10:
        return sorted(arr)[k]

    # Split arr into sublists of 5
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Find the median of medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partitioning step
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return median_of_medians(high, k - len(low) - pivot_count)

# Example usage
arr = [12, 3, 5, 7, 19]
k = 2
print(median_of_medians(arr, k))  # Expected Output: 5
