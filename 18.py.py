'''
18.Implement the Merge Sort algorithm in a programming language of your choice and test it on the array 12,4,78,23,45,67,89,1. Modify your implementation to count the number of comparisons made during the sorting process. Print this count along with the sorted array.
Test Cases :
Input : N= 8, a[] = {12,4,78,23,45,67,89,1}
Output :1,4,12,23,45,67,78,89
Test Cases :
Input : N= 7, a[] = {38,27,43,3,9,82,10}
Output :3,9,10,27,38,43,82.

All Pairs Shortest Paths: Floyd's Algorithm

'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        global comparison_count
        while i < len(left_half) and j < len(right_half):
            comparison_count += 1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

comparison_count = 0
array = [12, 4, 78, 23, 45, 67, 89, 1]
merge_sort(array)
print(f"Sorted array: {array}")
print(f"Number of comparisons: {comparison_count}")
