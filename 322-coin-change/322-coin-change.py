class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def findAnswer(i,arr,target,dp):

            if i == 0:
                if target%arr[i] == 0:
                    return target//arr[i]
                return float("inf")

            if dp[i][target] != -1:
                return dp[i][target]

            not_pick = findAnswer(i-1,arr,target,dp)
            pick = float("inf")
            if target >= arr[i]:
                pick = 1 + findAnswer(i,arr,target-arr[i],dp)

            dp[i][target] = min(pick,not_pick)
            return dp[i][target]
        
        dp = [[-1 for j in range(amount + 1)] for i in range(len(coins))]
        ans = findAnswer(len(coins)-1,coins,amount,dp)
        if ans >= float("inf"):
            return -1
        return ans

                
            
        