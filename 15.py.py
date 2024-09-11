'''15.Write a Program to find both the maximum and minimum values in the array.  Implement using any programming language of your choice.  Execute your code and provide the maximum and minimum values found. 
Input : N= 8, a[] = {5,7,3,4,9,12,6,2}
Output : Min = 2, Max = 12
Test Cases :
Input :N= 9, a[] = {1,3,5,7,9,11,13,15,17}
Output : Min = 1, Max = 17
Test Cases :
Input : N= 10, a[] = {22,34,35,36,43,67, 12,13,15,17}
Output : Min 12, Max 67
'''
def find_min_max(arr):
    min_value = min(arr)
    max_value = max(arr)
    return min_value, max_value

# Input
N = 8
a = [5, 7, 3, 4, 9, 12, 6, 2]

# Execution
min_value, max_value = find_min_max(a)

# Output
print(f"Min = {min_value}, Max = {max_value}")
