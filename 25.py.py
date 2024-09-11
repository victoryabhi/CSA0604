'''
25.You are tasked with designing an efficient coading to generate all subsets of a given set S containing n elements. Each subset should be outputted in lexicographical order. Return a list of lists where each inner list is a subset of the given set.Additionally, find out how your coading handles duplicate elements in S.
A = [1, 2, 3] The subsets of [1, 2, 3] are: [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]

'''
def subsets_with_dup(S):
    S.sort()  # Sort the input to ensure lexicographical order
    result = []
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(S)):
            if i > start and S[i] == S[i - 1]:  # Skip duplicates
                continue
            backtrack(i + 1, path + [S[i]])
    
    backtrack(0, [])
    return result

# Example usage
A = [1, 2, 3]
print(subsets_with_dup(A))
