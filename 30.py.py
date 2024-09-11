'''
30.You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security systems connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
(i)Input : nums = [2, 3, 2]
Output : The maximum money you can rob without alerting the 
police is 3(robbing house 1).
(i)Input : nums = [1, 2, 3, 1]
Output : The maximum money you can rob without alerting the 
police is 4 (robbing house 1 and house 3).

Mathematical Analysis of Non-Recursive Algorithms



'''
def rob_linear(nums):
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(prev + num, curr)
    return curr

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Example usage
print(rob([2, 3, 2]))  # Output: 3
print(rob([1, 2, 3, 1]))  # Output: 4
