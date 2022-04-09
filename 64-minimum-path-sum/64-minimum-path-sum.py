class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                # print (dp)
                if i == 0 and j == 0 : dp[i][j] = grid[i][j]
                
                else:
                    up = grid[i][j]
                    if i>0: up += dp[i-1][j]
                    else: up += 9999
                    
                    left = grid[i][j]
                    if j>0: left += dp[i][j-1]
                    else: left += 9999
                    
                    dp[i][j] = min(left,up)
        
        return dp[m-1][n-1]
        