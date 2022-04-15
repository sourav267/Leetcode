class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1 for j in range(m+1)] for i in range(n+1)]
        s1 = word1
        s2 = word2
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
        
        return n+m - dp[n][m] * 2
        