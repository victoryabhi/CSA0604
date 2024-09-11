'''
26. Write a program to implement the concept of subset generation. Given a set of unique integers and a specific integer 3, generate all subsets that contain the element 3. Return a list of lists where each inner list is a subset containing the element 3
E = [2, 3, 4, 5], x = 3,
The subsets containing 3 : [3], [2, 3], [3, 4], [3, 5], [2, 3, 4], [2, 3, 5], [3, 4, 5], [2, 3, 4, 5]

'''
def generate_subsets_with_element(E, x):
    def backtrack(start, path):
        if x in path:
            result.append(path)
        for i in range(start, len(E)):
            backtrack(i + 1, path + [E[i]])

    result = []
    backtrack(0, [])
    return result

# Example usage
E = [2, 3, 4, 5]
x = 3
subsets_with_3 = generate_subsets_with_element(E, x)
print("The subsets containing 3:", subsets_with_3)
