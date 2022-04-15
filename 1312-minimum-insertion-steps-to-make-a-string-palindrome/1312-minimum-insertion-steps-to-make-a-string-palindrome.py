class Solution:
    def minInsertions(self, s: str) -> int:


        n = len(s)
        m = len(s)
        dp = [[-1 for j in range(m+1)] for i in range(n+1)]
        s1 = s
        s2 = s[::-1]
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
        
        return len(s)-dp[n][m]
        