'''
16.Consider an array of integers sorted in ascending order: 2,4,6,8,10,12,14,18.
Write a Program to find both the maximum and minimum values in the array.  Implement using any programming language of your choice. Execute your code and provide the maximum and minimum values found. 
Input :N=8, 2,4,6,8,10,12,14,18.
Output : Min = 2, Max =18
Test Cases :
Input : N= 9, a[] = {11,13,15,17,19,21,23,35,37}
Output : Min = 11, Max = 37
Test Cases :
Input : N= 10, a[] = {22,34,35,36,43,67, 12,13,15,17}
Output : Min 12, Max 67

Merge Sort

'''
# Define the array
array = [2, 4, 6, 8, 10, 12, 14, 18]

# Find minimum and maximum values
min_value = min(array)
max_value = max(array)

# Output the results
print(f"Min = {min_value}, Max = {max_value}")
