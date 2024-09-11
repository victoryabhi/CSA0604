'''
28. Write a program to implement Meet in the Middle Technique. Given a large array of integers and an exact sum E, determine if there is any subset that sums exactly to E. Utilize the Meet in the Middle technique to handle the potentially large size of the array. Return true if there is a subset that sums exactly to E, otherwise return false.
a) E = {1, 3, 9, 2, 7, 12} exact Sum = 15
b) E = {3, 34, 4, 12, 5, 2} exact Sum = 15
Mathematical Analysis of Recursive Algorithms

'''
from itertools import combinations

def subset_sum(arr, target):
    n = len(arr)
    mid = n // 2
    
    # Generate all possible subset sums for the first half
    left_sums = {sum(comb) for i in range(mid + 1) for comb in combinations(arr[:mid], i)}
    
    # Generate all possible subset sums for the second half
    right_sums = {sum(comb) for i in range(n - mid + 1) for comb in combinations(arr[mid:], i)}
    
    # Check if there exists a pair of sums that equals the target
    for left in left_sums:
        if (target - left) in right_sums:
            return True
    return False

# Example usage
print(subset_sum([1, 3, 9, 2, 7, 12], 15))  # Output: True
print(subset_sum([3, 34, 4, 12, 5, 2], 15))  # Output: True
