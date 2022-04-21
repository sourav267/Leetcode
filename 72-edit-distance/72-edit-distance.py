class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def f(i, j, s1, s2, dp):
            if i == 0:
                return j

            if j == 0:
                return i

            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i-1] == s2[j-1]:
                dp[i][j] = f(i-1, j-1, s1, s2, dp)
                return dp[i][j]

            insert = 1 + f(i, j-1, s1, s2, dp)
            delete = 1 + f(i-1, j, s1, s2, dp)
            replace = 1 + f(i-1, j-1, s1, s2, dp)

            dp[i][j] = min(insert, delete, replace)
            return dp[i][j]
        
        n = len(word1)
        m = len(word2)
        dp = [[-1 for j in range(m+1)] for i in range(n+1)]
        ans = f(n, m, word1, word2, dp)
        return ans