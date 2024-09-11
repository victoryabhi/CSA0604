'''
29.Given an m x n grid and a ball at a starting cell, find the number of ways to move the ball out of the grid boundary in exactly N steps.
·Input: m=2,n=2,N=2,i=0,j=0·Output: 6
Input: m=1,n=3,N=3,i=0,j=1·Output: 12


'''
def findWays(m, n, N, i, j):
    dp = [[[0] * (N + 1) for _ in range(n)] for _ in range(m)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for step in range(1, N + 1):
        for x in range(m):
            for y in range(n):
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        dp[x][y][step] += 1
                    else:
                        dp[x][y][step] += dp[nx][ny][step - 1]
    
    return dp[i][j][N]

# Example usage:
print(findWays(2, 2, 2, 0, 0))  # Output: 6
print(findWays(1, 3, 3, 0, 1))  # Output: 12
