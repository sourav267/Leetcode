class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def f(i,j,s1,s2,dp):

            if j<0 and i<0:
                return True

            if i<0 and j>=0:
                return False

            if j<0 and i>=0:
                for k in range(i+1):
                    if s1[k] != '*':
                        return False
                return True

            if dp[i][j] != -1:
                return dp[i][j]
            
            if s1[i] == s2[j] or s1[i] == '?':
                dp[i][j] = f(i-1,j-1,s1,s2,dp)
                return dp[i][j]

            if s1[i] == '*':
                dp[i][j] = f(i-1,j,s1,s2,dp) or f(i,j-1,s1,s2,dp)
                return dp[i][j]
            
            dp[i][j] = False
            return dp[i][j]
        
        
        
        n = len(p)
        m = len(s)
        dp = [[-1 for j in range(m)] for i in range(n)]
        ans = f(n-1,m-1,p,s,dp)
        return ans
        