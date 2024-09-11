'''
MEET IN MIDDLE TECHNIQUE
27.Write a program to implement Meet in the Middle Technique. Given an array of integers and a target sum, find the subset whose sum is closest to the target. You will use the Meet in the Middle technique to efficiently find this subset.
a) Set[] = {45, 34, 4, 12, 5, 2} 	Target Sum : 42

b) Set[]= {1, 3, 2, 7, 4, 6}                    Target sum = 10:

'''
from itertools import combinations

def closest_subset_sum(arr, target):
    n = len(arr)
    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Generate all possible subset sums for both halves
    left_sums = {sum(comb) for r in range(len(left_half) + 1) for comb in combinations(left_half, r)}
    right_sums = {sum(comb) for r in range(len(right_half) + 1) for comb in combinations(right_half, r)}

    # Find the closest sum to the target
    closest_sum = float('inf')
    for left_sum in left_sums:
        for right_sum in right_sums:
            current_sum = left_sum + right_sum
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum

    return closest_sum

# Example usage
set_a = [45, 34, 4, 12, 5, 2]
target_a = 42
print("Closest sum to target in set A:", closest_subset_sum(set_a, target_a))

set_b = [1, 3, 2, 7, 4, 6]
target_b = 10
print("Closest sum to target in set B:", closest_subset_sum(set_b, target_b))
