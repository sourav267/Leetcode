class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         def findAnswer(s1,s2,i,j,dp):

#             if i == 0 or j == 0:
#                 return 0
            
#             if dp[i][j] != -1:
#                 return dp[i][j]

#             if s1[i-1] == s2[j-1]:
#                 dp[i][j] = 1 + findAnswer(s1,s2,i-1,j-1,dp)
#                 return dp[i][j]

#             dp[i][j] = max(findAnswer(s1,s2,i,j-1,dp),findAnswer(s1,s2,i-1,j,dp))
#             return dp[i][j]

        n = len(text1)
        m = len(text2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        s1 = text1
        s2 = text2
        for j in range(m+1):
            dp[0][j] = 0

        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i-1][j])
        
        return dp[n][m]
        