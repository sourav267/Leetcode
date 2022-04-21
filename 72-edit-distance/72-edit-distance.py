class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        for j in range(m+1):
            dp[0][j] = j

        for i in range(n+1):
            dp[i][0] = i

        for i in range(1, n+1):
            for j in range(1, m+1):

                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = dp[i][j - 1]
                    delete = dp[i-1][j]
                    replace = dp[i-1][j - 1]
                    dp[i][j] = 1 + min(insert, delete, replace)
        
        return dp[n][m]

#         def f(i, j, s1, s2, dp):
#             if i == 0:
#                 return j

#             if j == 0:
#                 return i

#             if dp[i][j] != -1:
#                 return dp[i][j]

#             if s1[i-1] == s2[j-1]:
#                 dp[i][j] = f(i-1, j-1, s1, s2, dp)
#                 return dp[i][j]

#             insert = 1 + f(i, j-1, s1, s2, dp)
#             delete = 1 + f(i-1, j, s1, s2, dp)
#             replace = 1 + f(i-1, j-1, s1, s2, dp)

#             dp[i][j] = min(insert, delete, replace)
#             return dp[i][j]
        
        # n = len(word1)
        # m = len(word2)
        # dp = [[-1 for j in range(m+1)] for i in range(n+1)]
        # ans = f(n, m, word1, word2, dp)
        # return ans