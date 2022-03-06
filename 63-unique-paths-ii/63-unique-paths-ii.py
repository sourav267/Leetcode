class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp =[[0 for _ in range(n)]] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 and obstacleGrid[i][j]==0:
                    dp[i][j] = 1
                else:
                    up = 0
                    left = 0
                    if i > 0 and obstacleGrid[i][j] == 0: up = dp[i-1][j]
                    if j > 0 and obstacleGrid[i][j] == 0: left = dp[i][j-1]
                    
                    dp[i][j] =  up + left
        return dp[m-1][n-1]
        # Recursion
        # def countPath(i,j,arr):
        #     if i==0 and j == 0 and arr[i][j] == 0:
        #         return 1
        #     if i<0 or j<0 or arr[i][j]==1:
        #         return 0
        #     return countPath(i-1,j,arr) + countPath(i,j-1,arr)
        # return countPath(len(obstacleGrid)-1,len(obstacleGrid[0])-1,obstacleGrid)

        