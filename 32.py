'''
32.A robot is located at the top-left corner of a m×n grid .The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there?
(i) Input: m=7,n=3      Output: 28
(ii) Input: m=3,n=2Output: 3

'''
import math

def unique_paths(m, n):
    return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))

# Example usage
print(unique_paths(7, 3))  # Output: 28
print(unique_paths(3, 2))  # Output: 3
