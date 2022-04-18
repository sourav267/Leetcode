class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def f(i,j,s,t,dp):
            if j<0:
                return 1
            if i<0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == t[j]:
                pick_both = f(i-1,j-1,s,t,dp)
                pick_one = f(i-1,j,s,t,dp)
                dp[i][j] = pick_both + pick_one
                return dp[i][j]
            else:
                dp[i][j] = f(i-1,j,s,t,dp)
                return dp[i][j] 
            
        n=len(s)
        m=len(t)
        dp=[[-1 for j in range(m)] for i in range(n)]
        ans = f(n-1,m-1,s,t,dp)
        return ans
        