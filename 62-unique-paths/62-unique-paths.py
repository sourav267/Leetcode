class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[0 for _ in range(n)]] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up = 0
                    left = 0
                    if i > 0: up = dp[i-1][j]
                    if j > 0: left = dp[i][j-1]
                    
                    dp[i][j] =  up + left
        return dp[m-1][n-1]
        
#         Recursion
#         def countPath(i,j):
#             if i==0 and j == 0:
#                 return 1
#             if i<0 or j<0:
#                 return 0
#             if dp[i][j] != -1: return dp[i][j]
#             dp[i][j] = countPath(i-1,j) + countPath(i,j-1)
#             return 
        
        
#         dp =[[-1 for _ in range(n)]] * m
#         # print (dp)
#         # return countPath(m-1,n-1,dp)


        