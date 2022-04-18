class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def f(i,j,s,t,dp):
            if j==0:
                return 1
            if i==0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i-1] == t[j-1]:
                pick_both = f(i-1,j-1,s,t,dp)
                pick_one = f(i-1,j,s,t,dp)
                dp[i][j] = pick_both + pick_one
                return dp[i][j]
            else:
                dp[i][j] = f(i-1,j,s,t,dp)
                return dp[i][j] 
            
        n=len(s)
        m=len(t)
        dp=[[0 for j in range(m+1)] for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=1
        
        for j in range(1,m+1):
            dp[0][j]=0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1] == t[j-1]:
                    pick_both = dp[i-1][j-1]
                    pick_one = dp[i-1][j]
                    dp[i][j] = pick_both + pick_one
                else:
                    dp[i][j] = dp[i-1][j] 
        
        # ans = f(n,m,s,t,dp)
        return dp[n][m]
        