class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k = sum(nums)
        n = len(nums)
        if k % 2 == 1:return False
        k = k//2
        dp = [[False for j in range(k + 1)] for i in range(n+1)]
        dp[0][0] = True
        
        for i in range(1,n+1):
            dp[i][0] = True
        
        for j in range(1,k+1):
            dp[0][j] = False

            
        for i in range(1,n+1):
            for j in range(1,k+1):
                notTake = dp[i-1][j]
                take = False
                if nums[i-1] <= j:
                    take = dp[i-1][j-nums[i-1]]
                dp[i][j] = take or notTake
        return dp[n][k];
        