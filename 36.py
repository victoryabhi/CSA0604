'''
36.Given four lists A, B, C, D of integer values,Write a program to 
compute how many tuples (i, j, k, l) there are such that 
A[i] + B[j] + C[k] + D[l] is zero.
(i)Input: A = [1, 2], B = [-2, -1], C = [-1, 2], D = [0, 2]
Output: 2
(i)Input: A = [0], B = [0], C = [0], D = [0]
Output: 1

'''
from collections import defaultdict

def count_tuples(A, B, C, D):
    sum_ab = defaultdict(int)
    
    # Calculate all possible sums of A[i] + B[j]
    for a in A:
        for b in B:
            sum_ab[a + b] += 1
            
    count = 0
    
    # Calculate all possible sums of C[k] + D[l] and check against sum_ab
    for c in C:
        for d in D:
            count += sum_ab[-(c + d)]
    
    return count

# Example usage
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
output = count_tuples(A, B, C, D)
print(output)  # Output: 2
