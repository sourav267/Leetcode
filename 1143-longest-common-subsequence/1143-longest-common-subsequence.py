class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def findAnswer(s1,s2,i,j,dp):

            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                dp[i][j] = 1 + findAnswer(s1,s2,i-1,j-1,dp)
                return dp[i][j]

            dp[i][j] = max(findAnswer(s1,s2,i,j-1,dp),findAnswer(s1,s2,i-1,j,dp))
            return dp[i][j]
        
        n = len(text1)
        m = len(text2)
        dp = [[-1 for j in range(m)] for i in range(n)]
        ans = findAnswer(text1,text2,n-1,m-1,dp)
        return ans
        