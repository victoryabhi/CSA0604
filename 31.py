'''
31.You are climbing a staircase. It takes nsteps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
(i) Input: n=4Output: 5
(ii) Input: n=3Output

'''
def climb_stairs(n):
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second

# Example usage:
print(climb_stairs(4))  # Output: 5
print(climb_stairs(3))  # Output: 3
